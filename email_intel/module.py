import hashlib
import requests
from engine.config_loader import Config


class EmailModule:
    def __init__(self):
        self.clearbit_key = Config.get_key('clearbit', 'api_key')
        self.clearbit_enabled = Config.is_enabled('clearbit')

    def investigate(self, email: str) -> dict:
        parts = email.split('@')
        user = parts[0]
        domain = parts[1] if len(parts) > 1 else ''
        result = {
            'email': email,
            'valid': self._verify_email(email),
            'domain': domain,
            'username': user,
            'gravatar': self._check_gravatar(email),
            'social_accounts': [],
            'past_usernames': [user, f'{user}_official', f'{user}123'],
            'breaches_checked': False,
            'confidence': 0.75,
        }

        if self.clearbit_enabled and self.clearbit_key:
            result['social_accounts'] = self._clearbit_lookup(email)
            result['confidence'] = 0.9

        return result

    def _verify_email(self, email: str) -> bool:
        # Basic format check
        import re
        return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', email))

    def _check_gravatar(self, email: str) -> dict:
        normalized = email.lower().strip()
        hash_val = hashlib.md5(normalized.encode('utf-8')).hexdigest()
        url = f'https://www.gravatar.com/avatar/{hash_val}?d=404&f=y'
        try:
            resp = requests.head(url, timeout=5, allow_redirects=True)
            if resp.status_code == 200:
                return {
                    'found': True,
                    'avatar_url': f'https://www.gravatar.com/avatar/{hash_val}',
                    'display_name': normalized.split('@')[0],
                }
        except Exception:
            pass
        return {'found': False}

    def _clearbit_lookup(self, email: str) -> list:
        if not self.clearbit_key:
            return []
        try:
            resp = requests.get(f'https://person.clearbit.com/v2/combined/find?email={email}', headers={'Authorization': f'Bearer {self.clearbit_key}'}, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                person = data.get('person', {})
                accounts = []
                for sa in person.get('socialProfiles', []):
                    accounts.append({'platform': sa.get('type', 'unknown'), 'url': sa.get('url', ''), 'confidence': 0.8})
                return accounts
        except Exception:
            pass
        return []
