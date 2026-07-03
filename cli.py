"""
OmniTrace — Universal Identity & Location Trace Engine
Command-line interface.

Developed by JOJIN JOHN.
"""

import sys
import argparse
import json

sys.path.insert(0, '.')

from engine.orchestrator import OmniTraceOrchestrator

__version__ = '1.0.0'

# Subcommands that the CLI understands. Anything else falls back to `trace`.
SUBCOMMANDS = {
    'trace', 'identify-place', 'check-username', 'investigate-email',
    'investigate-phone', 'search-breaches', 'search-social', 'search-darkweb',
    'monitor-darkweb', 'trace-crypto', 'analyze-document', 'whois',
    'dns-enum', 'ip-reputation',
}


def _dump(data) -> str:
    return json.dumps(data, indent=2, default=str)


def _emit(data, output='json', file=None):
    """Print or save a plain result dict."""
    text = _dump(data)
    if file:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved to {file}")
    else:
        print(text)


# --------------------------------------------------------------------------- #
# Console renderer for full dossiers (trace command)
# --------------------------------------------------------------------------- #
def print_console(dossier):
    print(f"\n{'='*60}")
    print("OMNITRACE DOSSIER")
    print(f"{'='*60}")
    print(f"Generated: {dossier.generated_at}")
    print(f"Confidence: {dossier.confidence_score}")
    print(f"\nTarget Inputs: {list(dossier.target.get('inputs', []))}")
    for k in ('name', 'email', 'phone', 'username'):
        if dossier.target.get(k):
            print(f"{k.capitalize()}: {dossier.target.get(k)}")

    print(f"\n{'-'*60}\nFINDINGS\n{'-'*60}")
    findings = dossier.findings

    if findings.get('people_search'):
        ps = findings['people_search']
        print(f"\n[+] People Search: {ps.get('query', 'N/A')}")
        for r in ps.get('results', []):
            print(f"    - {r.get('source', 'Unknown')} | confidence: {r.get('confidence', 0)}")

    if findings.get('social'):
        print("\n[+] Social Media Profiles:")
        for platform, data in findings['social'].items():
            if data.get('found'):
                print(f"    - {platform}: {data.get('url', 'N/A')} (confidence: {data.get('confidence', 0)})")

    if findings.get('email_info'):
        ei = findings['email_info']
        print(f"\n[+] Email Intel ({ei.get('email', 'N/A')}):")
        print(f"    Valid: {ei.get('valid', 'unknown')}")
        if ei.get('gravatar', {}).get('found'):
            print("    Gravatar: YES")
        for sa in ei.get('social_accounts', []):
            print(f"    Linked: {sa.get('platform')} - {sa.get('url', 'N/A')}")

    if findings.get('phone_info'):
        pi = findings['phone_info']
        print(f"\n[+] Phone Intel ({pi.get('phone', 'N/A')}):")
        print(f"    Carrier: {pi.get('carrier', 'unknown')}")
        print(f"    Type: {pi.get('line_type', 'unknown')}")
        print(f"    Location: {pi.get('location', {}).get('city', 'unknown')}")

    if findings.get('username_matches'):
        um = findings['username_matches']
        found = [k for k, v in um.items() if v.get('found')]
        print(f"\n[+] Username Matches: {len(found)} platforms found")
        for p in found[:10]:
            print(f"    - {p}: {um[p].get('url', 'N/A')}")
        if len(found) > 10:
            print(f"    ... and {len(found) - 10} more")

    if findings.get('breaches'):
        print("\n[+] Breach Data:")
        for key, data in findings['breaches'].items():
            if data.get('breaches_found', 0) > 0:
                print(f"    - {key}: {data.get('breaches_found', 0)} breaches from {', '.join(data.get('sources', []))}")

    if findings.get('darkweb'):
        dw = findings['darkweb']
        print(f"\n[+] Dark Web Mentions: {dw.get('total_matches', 0)}")
        for r in dw.get('results', []):
            print(f"    - {r.get('site', 'Unknown')} | {r.get('type', 'mention')} | risk: {r.get('risk_level', 'unknown')}")

    if findings.get('face_matches'):
        fm = findings['face_matches']
        n = len(fm.get('matches', fm.get('results', {})))
        print(f"\n[+] Face Matches: {n} platforms")

    if findings.get('reverse_image'):
        ri = findings['reverse_image']
        print(f"\n[+] Reverse Image: {ri.get('total_web_matches', 0)} matches found")

    if findings.get('exif'):
        ex = findings['exif']
        if ex.get('exif_found'):
            print(f"\n[+] EXIF: Camera {ex.get('camera', {}).get('model', 'unknown')}, Location {ex.get('location', 'unknown')}")

    print(f"\n{'='*60}\n")


# --------------------------------------------------------------------------- #
# Command handlers
# --------------------------------------------------------------------------- #
def cmd_trace(args):
    input_data = {}
    for k in ('name', 'email', 'phone', 'username', 'photo'):
        v = getattr(args, k, None)
        if v:
            input_data[k] = v

    if not input_data:
        print("Error: provide at least one of --name --email --phone --username --photo")
        return 1

    orchestrator = OmniTraceOrchestrator()
    dossier = orchestrator.trace(input_data)

    if args.output == 'json':
        _emit(dossier.to_dict(), 'json', args.file)
    elif args.output in ('html', 'pdf'):
        from output.module import OutputModule
        result = OutputModule().generate(dossier.to_dict(), fmt=args.output)
        if args.file:
            with open(args.file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Saved to {args.file}")
        else:
            print(result)
    else:  # console
        if args.file:
            with open(args.file, 'w', encoding='utf-8') as f:
                f.write(_dump(dossier.to_dict()))
            print(f"Saved to {args.file}")
        print_console(dossier)
    return 0


def cmd_identify_place(args):
    from location.module import LocationModule
    result = LocationModule().identify_place(args.photo)
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_check_username(args):
    from username.module import UsernameModule
    mod = UsernameModule()
    usernames = []
    if args.usernames_file:
        with open(args.usernames_file, 'r', encoding='utf-8') as f:
            usernames = [ln.strip() for ln in f if ln.strip()]
    elif args.username:
        usernames = [args.username]
    else:
        print("Error: provide --username or --usernames-file")
        return 1
    results = {u: mod.check(u) for u in usernames}
    out = results if len(results) > 1 else next(iter(results.values()))
    _emit(out, 'json', getattr(args, 'file', None))
    return 0


def cmd_investigate_email(args):
    from email_intel.module import EmailModule
    from breach.module import BreachModule
    result = EmailModule().investigate(args.email)
    if args.breaches:
        result['breaches'] = BreachModule().search({'email': args.email})
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_investigate_phone(args):
    from phone.module import PhoneModule
    result = PhoneModule().lookup(args.phone)
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_search_breaches(args):
    from breach.module import BreachModule
    from username.breach.breach_db import BreachDatabase
    leads = {}
    if args.email:
        leads['email'] = args.email
    if args.username:
        leads['username'] = args.username
    result = BreachModule().search(leads) if leads else {}
    if args.password:
        result['password'] = BreachDatabase().search_by_password(args.password)
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_search_social(args):
    from social.module import SocialModule
    leads = {}
    if args.name:
        leads['name'] = args.name
    result = SocialModule().search_all(leads)
    if args.platform:
        result = {args.platform: result.get(args.platform, {'found': False})}
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_search_darkweb(args):
    from darkweb.module import DarkWebModule
    leads = {}
    if args.name:
        leads['name'] = args.name
    if args.email:
        leads['email'] = args.email
    result = DarkWebModule().search(leads)
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_monitor_darkweb(args):
    from darkweb.module import DarkWebModule
    leads = {}
    if args.name:
        leads['name'] = args.name
    if args.email:
        leads['email'] = args.email
    result = DarkWebModule().search(leads)
    result['monitoring'] = {
        'continuous': bool(args.continuous),
        'interval': args.interval,
        'note': 'One-shot scan. Continuous monitoring requires a scheduler/daemon.',
    }
    _emit(result, 'json', args.output if getattr(args, 'output', None) else None)
    return 0


def cmd_trace_crypto(args):
    from crypto.module import CryptoModule
    mod = CryptoModule()
    if args.btc:
        result = mod.trace(args.btc, chain='btc')
    elif args.eth:
        result = mod.trace(args.eth, chain='eth')
    elif args.name:
        result = mod.find_wallet({'name': args.name})
    else:
        print("Error: provide --btc, --eth, or --name")
        return 1
    _emit(result, 'json', getattr(args, 'file', None))
    return 0


def cmd_analyze_document(args):
    from document.module import DocumentModule
    mod = DocumentModule()
    if args.stego:
        result = mod.check_stego(args.file)
    else:
        result = mod.analyze(args.file)
    _emit(result, 'json', None)
    return 0


def cmd_whois(args):
    from network.module import NetworkModule
    _emit(NetworkModule().whois(args.domain), 'json', None)
    return 0


def cmd_dns_enum(args):
    from network.module import NetworkModule
    _emit(NetworkModule().dns_enum(args.domain), 'json', None)
    return 0


def cmd_ip_reputation(args):
    from network.module import NetworkModule
    _emit(NetworkModule().ip_reputation(args.ip), 'json', None)
    return 0


# --------------------------------------------------------------------------- #
# Argument parsing
# --------------------------------------------------------------------------- #
def build_parser():
    parser = argparse.ArgumentParser(
        prog='omnitrace',
        description='OmniTrace — Universal Identity & Location Trace Engine (by JOJIN JOHN)',
    )
    parser.add_argument('--version', action='version', version=f'OmniTrace {__version__}')
    sub = parser.add_subparsers(dest='command')

    # trace
    p = sub.add_parser('trace', help='Full identity trace from any input(s)')
    p.add_argument('--name')
    p.add_argument('--email')
    p.add_argument('--phone')
    p.add_argument('--username')
    p.add_argument('--photo')
    p.add_argument('--mode', default='quick', choices=['quick', 'normal', 'deep'])
    p.add_argument('--output', default='console', choices=['console', 'html', 'pdf', 'json'])
    p.add_argument('--file')
    p.add_argument('--graph', action='store_true')
    p.add_argument('--face-search', dest='face_search', action='store_true')
    p.add_argument('--exif-only', dest='exif_only', action='store_true')
    p.add_argument('--identify-place', dest='identify_place', action='store_true')
    p.add_argument('--platforms')
    p.add_argument('--export', choices=['neo4j', 'd3', 'png'])
    p.set_defaults(func=cmd_trace)

    # identify-place
    p = sub.add_parser('identify-place', help='Identify a location from a photo')
    p.add_argument('--photo', required=True)
    p.add_argument('--details', action='store_true')
    p.add_argument('--nearby', action='store_true')
    p.add_argument('--map', action='store_true')
    p.add_argument('--file')
    p.set_defaults(func=cmd_identify_place)

    # check-username
    p = sub.add_parser('check-username', help='Check a username across platforms')
    p.add_argument('--username')
    p.add_argument('--usernames-file', dest='usernames_file')
    p.add_argument('--output', default='json', choices=['json', 'console'])
    p.add_argument('--file')
    p.set_defaults(func=cmd_check_username)

    # investigate-email
    p = sub.add_parser('investigate-email', help='Investigate an email address')
    p.add_argument('--email', required=True)
    p.add_argument('--breaches', action='store_true')
    p.add_argument('--social', action='store_true')
    p.add_argument('--gravatar', action='store_true')
    p.add_argument('--file')
    p.set_defaults(func=cmd_investigate_email)

    # investigate-phone
    p = sub.add_parser('investigate-phone', help='Investigate a phone number')
    p.add_argument('--phone', required=True)
    p.add_argument('--carrier', action='store_true')
    p.add_argument('--social', action='store_true')
    p.add_argument('--reputation', action='store_true')
    p.add_argument('--file')
    p.set_defaults(func=cmd_investigate_phone)

    # search-breaches
    p = sub.add_parser('search-breaches', help='Search breach databases')
    p.add_argument('--email')
    p.add_argument('--username')
    p.add_argument('--password')
    p.add_argument('--export-creds', dest='export_creds', action='store_true')
    p.add_argument('--file')
    p.set_defaults(func=cmd_search_breaches)

    # search-social
    p = sub.add_parser('search-social', help='Search social media')
    p.add_argument('--name')
    p.add_argument('--platform')
    p.add_argument('--category')
    p.add_argument('--scrape-all', dest='scrape_all', action='store_true')
    p.add_argument('--file')
    p.set_defaults(func=cmd_search_social)

    # search-darkweb
    p = sub.add_parser('search-darkweb', help='Search the dark web')
    p.add_argument('--name')
    p.add_argument('--email')
    p.add_argument('--file')
    p.set_defaults(func=cmd_search_darkweb)

    # monitor-darkweb
    p = sub.add_parser('monitor-darkweb', help='Monitor the dark web for mentions')
    p.add_argument('--name')
    p.add_argument('--email')
    p.add_argument('--continuous', action='store_true')
    p.add_argument('--interval', default='24h')
    p.add_argument('--alert')
    p.add_argument('--output')
    p.set_defaults(func=cmd_monitor_darkweb)

    # trace-crypto
    p = sub.add_parser('trace-crypto', help='Trace a cryptocurrency address')
    p.add_argument('--btc')
    p.add_argument('--eth')
    p.add_argument('--name')
    p.add_argument('--file')
    p.set_defaults(func=cmd_trace_crypto)

    # analyze-document
    p = sub.add_parser('analyze-document', help='Analyze a document / image file')
    p.add_argument('--file', required=True)
    p.add_argument('--stego', action='store_true')
    p.add_argument('--ocr', action='store_true')
    p.set_defaults(func=cmd_analyze_document)

    # whois
    p = sub.add_parser('whois', help='WHOIS lookup for a domain')
    p.add_argument('--domain', required=True)
    p.set_defaults(func=cmd_whois)

    # dns-enum
    p = sub.add_parser('dns-enum', help='DNS enumeration for a domain')
    p.add_argument('--domain', required=True)
    p.set_defaults(func=cmd_dns_enum)

    # ip-reputation
    p = sub.add_parser('ip-reputation', help='Check IP reputation')
    p.add_argument('--ip', required=True)
    p.set_defaults(func=cmd_ip_reputation)

    return parser


def main():
    argv = sys.argv[1:]

    # Backward compatibility: `python cli.py --name X` (no subcommand) -> trace
    if argv and argv[0].startswith('-') and argv[0] not in ('--version', '-h', '--help'):
        argv = ['trace'] + argv

    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, 'command', None):
        parser.print_help()
        return 1

    return args.func(args) or 0


if __name__ == '__main__':
    sys.exit(main())
