import sys
import argparse
import json
import yaml
sys.path.insert(0, '.')
from engine.orchestrator import OmniTraceOrchestrator


def print_console(dossier):
    print(f"\n{'='*60}")
    print(f"OMNITRACE DOSSIER")
    print(f"{'='*60}")
    print(f"Generated: {dossier.generated_at}")
    print(f"Confidence: {dossier.confidence_score}")
    print(f"\nTarget Inputs: {list(dossier.target.get('inputs', []))}")
    if dossier.target.get('name'):
        print(f"Name: {dossier.target.get('name')}")
    if dossier.target.get('email'):
        print(f"Email: {dossier.target.get('email')}")
    if dossier.target.get('phone'):
        print(f"Phone: {dossier.target.get('phone')}")
    if dossier.target.get('username'):
        print(f"Username: {dossier.target.get('username')}")
    
    print(f"\n{'-'*60}")
    print("FINDINGS")
    print(f"{'-'*60}")
    
    findings = dossier.findings
    if findings.get('people_search'):
        ps = findings['people_search']
        print(f"\n[+] People Search: {ps.get('query', 'N/A')}")
        for r in ps.get('results', []):
            print(f"    - {r.get('source', 'Unknown')} | confidence: {r.get('confidence', 0)}")
    
    if findings.get('social'):
        print(f"\n[+] Social Media Profiles:")
        for platform, data in findings['social'].items():
            if data.get('found'):
                print(f"    - {platform}: {data.get('url', 'N/A')} (confidence: {data.get('confidence', 0)})")
    
    if findings.get('email_info'):
        ei = findings['email_info']
        print(f"\n[+] Email Intel ({ei.get('email', 'N/A')}):")
        print(f"    Valid: {ei.get('valid', 'unknown')}")
        if ei.get('gravatar', {}).get('found'):
            print(f"    Gravatar: YES")
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
        br = findings['breaches']
        print(f"\n[+] Breach Data:")
        for key, data in br.items():
            if data.get('breaches_found', 0) > 0:
                print(f"    - {key}: {data.get('breaches_found', 0)} breaches from {', '.join(data.get('sources', []))}")
    
    if findings.get('darkweb'):
        dw = findings['darkweb']
        print(f"\n[+] Dark Web Mentions: {dw.get('total_matches', 0)}")
        for r in dw.get('results', []):
            print(f"    - {r.get('site', 'Unknown')} | {r.get('type', 'mention')} | risk: {r.get('risk_level', 'unknown')}")
    
    if findings.get('face_matches'):
        fm = findings['face_matches']
        print(f"\n[+] Face Matches: {len(fm.get('results', {}))} platforms")
    
    if findings.get('reverse_image'):
        ri = findings['reverse_image']
        print(f"\n[+] Reverse Image: {ri.get('total_web_matches', 0)} matches found")
    
    if findings.get('exif'):
        ex = findings['exif']
        if ex.get('exif_found'):
            print(f"\n[+] EXIF: Camera {ex.get('camera', {}).get('model', 'unknown')}, Location {ex.get('location', 'unknown')}")
    
    print(f"\n{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description='OmniTrace CLI')
    parser.add_argument('--name', help='Name to trace')
    parser.add_argument('--email', help='Email to trace')
    parser.add_argument('--phone', help='Phone to trace')
    parser.add_argument('--username', help='Username to trace')
    parser.add_argument('--photo', help='Photo path')
    parser.add_argument('--mode', default='quick', choices=['quick', 'normal', 'deep'])
    parser.add_argument('--output', default='console', choices=['console', 'html', 'pdf', 'json'])
    parser.add_argument('--file', help='Output file')
    parser.add_argument('--graph', action='store_true')
    parser.add_argument('--face-search', action='store_true')
    parser.add_argument('--identify-place', action='store_true')
    parser.add_argument('--exif-only', action='store_true')
    parser.add_argument('--check-username', action='store_true')
    parser.add_argument('--investigate-email', action='store_true')
    parser.add_argument('--investigate-phone', action='store_true')
    args = parser.parse_args()

    input_data = {}
    if args.name:
        input_data['name'] = args.name
    if args.email:
        input_data['email'] = args.email
    if args.phone:
        input_data['phone'] = args.phone
    if args.username:
        input_data['username'] = args.username
    if args.photo:
        input_data['photo'] = args.photo

    if not input_data:
        parser.print_help()
        sys.exit(1)

    orchestrator = OmniTraceOrchestrator()
    dossier = orchestrator.trace(input_data)

    if args.output == 'json':
        result = json.dumps(dossier.to_dict(), indent=2, default=str)
    elif args.output in ('html', 'pdf'):
        from output.module import OutputModule
        result = OutputModule().generate(dossier.to_dict(), fmt=args.output)
    else:
        if args.file:
            result = json.dumps(dossier.to_dict(), indent=2, default=str)
            with open(args.file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Saved to {args.file}")
        print_console(dossier)
        return

    if args.file:
        with open(args.file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"Saved to {args.file}")
    else:
        print(result)


if __name__ == '__main__':
    main()
