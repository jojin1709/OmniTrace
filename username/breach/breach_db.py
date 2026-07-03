"""
Search through billions of breached records for associated data
"""

class BreachDatabase:
    def __init__(self):
        self.breach_sources = [
            # Local breach dumps (downloaded by user)
            'HaveIBeenPwned', 'DeHashed', 'LeakCheck', 'IntelX',
            'SnusBase', 'Scylla', 'COMB', 'Collection1-5',
            'Exploit.in', 'AntiPublic', 'Verifications.io',
            'LinkedIn', 'Facebook', 'Adobe', 'Last.fm',
            'MySpace', 'Netflix', 'Dropbox', 'Tumblr',
            'Ashley Madison', 'Adult FriendFinder',
        ]
    
    def search_by_email(self, email: str) -> dict:
        """Search for email in all breach databases"""
        results = {}
        for source in self.breach_sources:
            records = self._query(source, 'email', email)
            if records:
                results[source] = {
                    'found': True,
                    'records': records[:10],  # Top 10
                    'total': len(records),
                    'passwords': [r.get('password') for r in records if r.get('password')],
                    'plaintext_passwords': any(r.get('is_plaintext') for r in records),
                }
        return results
    
    def search_by_username(self, username: str) -> dict:
        results = {}
        for source in self.breach_sources:
            records = self._query(source, 'username', username)
            if records:
                results[source] = records[:10]
        return results
    
    def search_by_password(self, password: str) -> dict:
        """Check if password appears in breaches (reuse detection)"""
        results = {'found': False, 'count': 0, 'samples': []}
        for source in self.breach_sources:
            records = self._query(source, 'password', password)
            if records:
                results['found'] = True
                results['count'] += len(records)
                results['samples'].extend([r.get('email') for r in records[:5]])
        return results
    
    def password_reuse_analysis(self, found_passwords: list) -> dict:
        """Analyze password patterns and reuse"""
        found_passwords = found_passwords or []
        return {
            'most_common': self._most_common(found_passwords),
            'patterns': self._find_patterns(found_passwords),
            'strength': self._assess_strength(found_passwords),
            'related_accounts': self._find_accounts_sharing_password(found_passwords),
        }

    def _query(self, source: str, field: str, value: str) -> list:
        """Query a single breach source. Returns matching records.

        Placeholder implementation: real deployments plug local breach
        dumps in here. Returns an empty list so callers degrade gracefully.
        """
        return []

    def _most_common(self, passwords: list) -> list:
        """Return the most frequently occurring passwords."""
        counts = {}
        for pw in passwords:
            counts[pw] = counts.get(pw, 0) + 1
        return sorted(counts, key=counts.get, reverse=True)[:10]

    def _find_patterns(self, passwords: list) -> list:
        """Detect simple reuse patterns across passwords."""
        patterns = []
        if any(p and p.isdigit() for p in passwords):
            patterns.append('numeric_only')
        if any(p and p.isalpha() for p in passwords):
            patterns.append('alpha_only')
        return patterns

    def _assess_strength(self, passwords: list) -> str:
        """Rough strength assessment for a set of passwords."""
        if not passwords:
            return 'unknown'
        avg_len = sum(len(p) for p in passwords if p) / max(len(passwords), 1)
        if avg_len >= 12:
            return 'strong'
        if avg_len >= 8:
            return 'medium'
        return 'weak'

    def _find_accounts_sharing_password(self, passwords: list) -> list:
        """Find accounts that reuse the same password."""
        return []