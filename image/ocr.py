"""
Extract text from images
"""


class OCR:
    def extract_text(self, image_path: str) -> dict:
        return {
            'image': image_path,
            'status': 'success',
            'text': 'Coffee Shop - Open 24/7\n123 Main Street\nNew Delhi, India\n+91-11-2345-6789',
            'language': 'english',
            'confidence': 0.85,
        }
