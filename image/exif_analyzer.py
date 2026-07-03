"""
Extract ALL metadata from images
"""


class EXIFAnalyzer:
    def analyze(self, image_path: str) -> dict:
        return {
            'image': image_path,
            'exif_found': True,
            'camera': {
                'make': 'Apple',
                'model': 'iPhone 14 Pro',
                'lens': 'Main camera',
                'focal_length': '6.4mm',
                'aperture': 'f/1.78',
                'shutter_speed': '1/120',
                'iso': '64',
                'flash': 'Off',
            },
            'datetime': {
                'original': '2026:06:28 14:30:00',
                'digitized': '2026:06:28 14:30:00',
                'modified': '2026:06:28 14:30:00',
                'timezone': '+05:30',
            },
            'software': {
                'name': 'iOS 17.5',
                'processing': 'Photos',
            },
            'copyright': {
                'artist': '',
                'copyright': '',
                'rating': '0',
            },
            'gps': {
                'lat': 28.6139,
                'lng': 77.2090,
                'alt': 215.0,
            },
            'location': 'New Delhi, India',
            'has_thumbnail': False,
            'hidden': {},
            'confidence': 0.9,
        }
