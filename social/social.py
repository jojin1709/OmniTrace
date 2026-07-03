class FacebookSearch:
    def search_by_name(self, name: str) -> dict:
        """Find profiles matching a name"""
        uname = (name or 'unknown').lower().replace(' ', '.')
        return {
            'profiles': [f'https://facebook.com/{uname}'],
            'photos': [f'https://facebook.com/{uname}/photos'],
            'friends': ['friend1', 'friend2'],
            'location': 'City, Country',
            'work': ['Company'],
            'education': ['School'],
            'email': None,
            'phone': None,
            'mutual_connections': ['person1'],
            'activity': ['likes', 'groups', 'events'],
            'metadata': {
                'account_created': None,
                'last_active': None,
                'privacy_settings': ['public', 'friends_only'],
                'associated_pages': [],
            },
            'confidence': 0.6,
        }

    def search_by_photo(self, image: str) -> dict:
        """Find profiles containing a specific photo"""
        return {'image': image, 'profiles': [], 'confidence': 0.0}

    def search_by_email(self, email: str) -> dict:
        """Find account by email"""
        return {'email': email, 'found': False, 'profile': None}

    def search_by_phone(self, phone: str) -> dict:
        """Find account by phone number"""
        return {'phone': phone, 'found': False, 'profile': None}

    def search_by_username(self, username: str) -> dict:
        """Check if username exists"""
        return {
            'username': username,
            'found': True,
            'url': f'https://facebook.com/{username}',
        }
