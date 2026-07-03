import requests
import time
from engine.config_loader import Config


class BreachModule:
    def __init__(self):
        self.hibp_key = Config.get_key('haveibeenpwned', 'api_key')
        self.hibp_enabled = Config.is_enabled('haveibeenpwned')

    def search(self, leads: dict) -> dict:
        results = {}
        email = leads.get('email')
        if email:
            results['email'] = self._search_email(email)
        username = leads.get('username')
        if username:
            results['username'] = self._search_username(username)
        return results

    def _search_email(self, email: str) -> dict:
        if self.hibp_enabled and self.hibp_key:
            try:
                headers = {'hibp-api-key': self.hibp_key, 'User-Agent': 'OmniTrace'}
                resp = requests.get(f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false', headers=headers, timeout=10)
                if resp.status_code == 200:
                    breaches = resp.json()
                    return {
                        'searched': email,
                        'breaches_found': len(breaches),
                        'sources': [b.get('Name') for b in breaches],
                        'total_records': len(breaches),
                        'confidence': 0.95,
                    }
                elif resp.status_code == 404:
                    return {'searched': email, 'breaches_found': 0, 'sources': [], 'total_records': 0, 'confidence': 0.9}
            except Exception as e:
                return {'searched': email, 'error': str(e), 'fallback': True}
        
        # Fallback stub
        return {
            'searched': email,
            'breaches_found': 3,
            'sources': ['LinkedIn 2023', 'Adobe 2019', 'Dropbox 2012'],
            'total_records': 5,
            'passwords': ['j*****3!', 'a*****9'],
            'has_plaintext': True,
            'confidence': 0.7,
            'note': 'Mock data. Enable HaveIBeenPwned API for real results.',
        }

    def _search_username(self, username: str) -> dict:
        return {
            'searched': username,
            'breaches_found': 1,
            'sources': ['GamingPlatform 2021'],
            'total_records': 2,
            'confidence': 0.6,
            'note': 'Mock data. Enable breach API for real results.',
        }
