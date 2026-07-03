from .identity_graph import IdentityGraph


class CorrelationEngine:
    def build_graph(self, findings: dict, target: dict = None) -> dict:
        graph = IdentityGraph()
        return graph.build(findings, target or {})

    def score_confidence(self, findings: dict, graph_data: dict) -> float:
        score = 0.0
        weights = {
            'social': 0.2,
            'email_info': 0.25,
            'phone_info': 0.2,
            'username_matches': 0.2,
            'breaches': 0.1,
            'darkweb': 0.05,
            'people_search': 0.15,
        }
        max_score = sum(weights.values())
        for key, weight in weights.items():
            data = findings.get(key, {})
            if isinstance(data, dict):
                found = bool(data)
                score += weight if found else 0
            elif isinstance(data, list):
                score += weight if data else 0
        return round(min(score / max_score, 1.0), 2) if max_score else 0.0
