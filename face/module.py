from .face_search import FaceSearch


class FaceModule:
    def search(self, image_path: str) -> dict:
        return FaceSearch().search(image_path)
