from .dossier_html import HTMLDossier
from .dossier_json import JSONDossier
from .dossier_pdf import PDFDossier


class OutputModule:
    def generate(self, data: dict, fmt: str = 'html') -> str:
        if fmt == 'json':
            return JSONDossier().generate(data)
        if fmt == 'pdf':
            return PDFDossier().generate(data)
        return HTMLDossier().generate(data.get('graph', {}), data)
