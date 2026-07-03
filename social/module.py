import re


class SocialModule:
    def search_all(self, leads: dict) -> dict:
        name = leads.get('name', '')
        username = leads.get('username', '')
        email = leads.get('email', '')
        results = {}
        if name or username or email:
            platforms = ['facebook', 'twitter', 'linkedin', 'instagram', 'tiktok', 'reddit', 'github', 'youtube', 'pinterest', 'snapchat']
            for p in platforms:
                results[p] = self._mock_result(p, name, username, email)
        return results

    def _mock_result(self, platform: str, name: str, username: str, email: str) -> dict:
        uname = username or name.lower().replace(' ', '_')
        return {
            'platform': platform,
            'found': True,
            'url': f'https://{platform}.com/{uname}',
            'username': uname,
            'display_name': name or uname,
            'bio': f'Profile of {name or uname}',
            'followers': 1247,
            'following': 543,
            'posts_count': 892,
            'verified': platform == 'github',
            'last_active': '2026-06-28',
            'confidence': 0.8,
        }
