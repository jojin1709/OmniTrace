try:
    import whois as _whois
except Exception:  # pragma: no cover - optional dependency
    _whois = None


class WHOIS:
    def lookup(self, domain: str) -> dict:
        if _whois is None:
            return {'domain': domain, 'error': 'python-whois not installed'}
        try:
            data = _whois.whois(domain)
            return {'domain': domain, 'data': str(data)}
        except Exception as e:
            return {'domain': domain, 'error': str(e)}


class DNS:
    def enumerate(self, domain: str) -> dict:
        return {'domain': domain, 'records': []}


class DomainSearch:
    def search(self, query: str) -> dict:
        return {'query': query, 'results': []}


class IPReputation:
    def check(self, ip: str) -> dict:
        return {'ip': ip, 'reputation': 'unknown'}
