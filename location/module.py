from .place_identifier import PlaceIdentifier


class LocationModule:
    def identify_place(self, image_path: str) -> dict:
        return PlaceIdentifier().identify(image_path)
