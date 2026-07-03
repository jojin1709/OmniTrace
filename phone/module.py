import re


class PhoneModule:
    def lookup(self, phone: str) -> dict:
        digits = re.sub(r'[^\d]', '', phone)
        country = 'US'
        area = digits[1:4] if len(digits) >= 7 else '000'
        return {
            'phone': phone,
            'valid': True,
            'country': country,
            'carrier': 'T-Mobile',
            'line_type': 'mobile',
            'location': {
                'state': 'Illinois',
                'city': 'Chicago',
                'timezone': 'America/Chicago',
                'area_code': area,
            },
            'social_accounts': [
                {'platform': 'WhatsApp', 'found': True, 'confidence': 0.6},
                {'platform': 'Telegram', 'found': True, 'confidence': 0.5},
                {'platform': 'Signal', 'found': False, 'confidence': 0.2},
            ],
            'scam_reputation': 'low',
            'spam_score': 0.12,
            'confidence': 0.75,
        }
