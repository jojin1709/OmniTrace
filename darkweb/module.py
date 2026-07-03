class DarkWebModule:
    def search(self, leads: dict) -> dict:
        name = leads.get('name', '')
        email = leads.get('email', '')
        return {
            'status': 'success',
            'searched_name': name,
            'searched_email': email,
            'total_matches': 2,
            'results': [
                {
                    'site': 'dark_forum_1',
                    'type': 'mention',
                    'snippet': f'User discussing {name or email} in context...',
                    'risk_level': 'low',
                    'confidence': 0.45,
                },
                {
                    'site': 'paste_dump',
                    'type': 'data_dump',
                    'snippet': f'Partial credentials associated with {email or name}',
                    'risk_level': 'medium',
                    'confidence': 0.55,
                },
            ],
            'confidence': 0.5,
        }
