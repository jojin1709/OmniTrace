from datetime import datetime


class Dossier:
    def __init__(self, target=None, findings=None, graph=None, confidence_score=0.0):
        self.target = target or {}
        self.findings = findings or {}
        self.graph = graph or {}
        self.confidence_score = confidence_score
        self.generated_at = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            'target': self.target,
            'findings': self.findings,
            'graph': self.graph,
            'confidence_score': self.confidence_score,
            'generated_at': self.generated_at,
        }


class ReportGenerator:
    @staticmethod
    def build_dossier(target, findings, graph_data, confidence_score=0.0) -> Dossier:
        return Dossier(
            target=target,
            findings=findings,
            graph=graph_data,
            confidence_score=confidence_score,
        )
