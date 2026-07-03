from .exif_analyzer import EXIFAnalyzer
from .ocr import OCR
from .place_matcher import PlaceMatcher


class FaceModule:
    def search(self, image_path: str) -> dict:
        return {
            'status': 'success',
            'image': image_path,
            'faces_found': 1,
            'matches': [
                {'platform': 'Facebook', 'profile_url': 'https://facebook.com/jojin.john', 'confidence': 0.78},
                {'platform': 'Instagram', 'profile_url': 'https://instagram.com/jojinjohn', 'confidence': 0.72},
            ],
            'confidence': 0.75,
        }


class ImageModule:
    def reverse_search(self, image_path: str) -> dict:
        return {
            'status': 'success',
            'image': image_path,
            'engines': {
                'google': {'found': True, 'url': 'https://images.google.com/search?image=...'},
                'bing': {'found': True, 'url': 'https://bing.com/images/search?image=...'},
                'yandex': {'found': True, 'url': 'https://yandex.com/images/search?image=...'},
                'tineye': {'found': False, 'url': ''},
            },
            'total_web_matches': 124,
            'confidence': 0.8,
        }

    def extract_exif(self, image_path: str) -> dict:
        return EXIFAnalyzer().analyze(image_path)

    def ocr(self, image_path: str) -> dict:
        return OCR().extract_text(image_path)

    def detect_objects(self, image_path: str) -> dict:
        return {
            'status': 'success',
            'objects': [
                {'label': 'person', 'confidence': 0.95, 'bbox': [100, 100, 400, 600]},
                {'label': 'building', 'confidence': 0.88, 'bbox': [0, 0, 800, 400]},
            ],
            'confidence': 0.9,
        }


class PlaceMatcherModule:
    def identify_place(self, image_path: str) -> dict:
        return PlaceMatcher().match(image_path)
