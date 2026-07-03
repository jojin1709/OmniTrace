import re


class NameModule:
    def search(self, name: str) -> dict:
        parts = name.split()
        first = parts[0] if parts else name
        last = parts[-1] if len(parts) > 1 else ''
        return {
            'name': name,
            'query': name,
            'status': 'success',
            'total_results': 12,
            'results': [
                {
                    'source': 'people_search_engine_1',
                    'name': name,
                    'age': '32-38',
                    'locations': ['New York, USA', 'San Francisco, USA'],
                    'occupation': 'Software Engineer',
                    'education': 'State University',
                    'social_profiles': ['facebook.com/profile', 'linkedin.com/in/profile'],
                    'confidence': 0.85,
                },
                {
                    'source': 'people_search_engine_2',
                    'name': name,
                    'age': '30-40',
                    'locations': ['Chicago, USA'],
                    'occupation': 'Data Scientist',
                    'confidence': 0.72,
                },
                {
                    'source': 'news_archive',
                    'title': f'{name} mentioned in local news',
                    'url': 'https://example-news.com/article',
                    'snippet': f'{name} was recently featured in a technology conference...',
                    'confidence': 0.65,
                },
                {
                    'source': 'court_records',
                    'case_type': 'Traffic violation',
                    'date': '2019-03-15',
                    'status': 'Closed',
                    'confidence': 0.45,
                },
                {
                    'source': 'property_records',
                    'address': '123 Main St, Springfield, IL 62701',
                    'property_type': 'Residential',
                    'ownership': 'Owner',
                    'confidence': 0.78,
                },
            ],
        }
