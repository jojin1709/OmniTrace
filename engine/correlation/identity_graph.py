"""
Build a graph connecting all discovered identities, accounts, and locations
"""


class IdentityGraph:
    def __init__(self):
        self.graph = {
            'nodes': {},
            'edges': [],
        }
    
    def add_person(self, person_id: str, name: str, confidence: float):
        self.graph['nodes'][person_id] = {
            'type': 'person',
            'label': name,
            'confidence': confidence,
            'attributes': {},
        }
    
    def add_account(self, account_id: str, platform: str, username: str, url: str):
        self.graph['nodes'][account_id] = {
            'type': 'account',
            'label': f'{platform}: {username}',
            'platform': platform,
            'username': username,
            'url': url,
        }
    
    def add_email(self, email_id: str, email: str):
        self.graph['nodes'][email_id] = {
            'type': 'email',
            'label': email,
            'email': email,
        }
    
    def add_phone(self, phone_id: str, phone: str, carrier: str = ''):
        self.graph['nodes'][phone_id] = {
            'type': 'phone',
            'label': phone,
            'phone': phone,
            'carrier': carrier,
        }
    
    def add_location(self, location_id: str, address: str, lat: float, lng: float):
        self.graph['nodes'][location_id] = {
            'type': 'location',
            'label': address,
            'lat': lat,
            'lng': lng,
            'address': address,
        }
    
    def add_photo(self, photo_id: str, url: str, thumbnail: str = ''):
        self.graph['nodes'][photo_id] = {
            'type': 'photo',
            'label': 'Photo',
            'url': url,
            'thumbnail': thumbnail or url,
        }
    
    def add_connection(self, source: str, target: str, relationship: str, confidence: float = 1.0):
        self.graph['edges'].append({
            'source': source,
            'target': target,
            'relationship': relationship,
            'confidence': confidence,
        })
    
    def build(self, findings: dict, target: dict) -> dict:
        self.graph = {'nodes': {}, 'edges': []}
        person_id = 'person_1'
        name = target.get('name', 'Unknown')
        self.add_person(person_id, name, 0.85)
        
        accounts = findings.get('social', {})
        for platform, data in accounts.items():
            if data.get('found'):
                acc_id = f'acc_{platform}'
                self.add_account(acc_id, platform, data.get('username', ''), data.get('url', ''))
                self.add_connection(person_id, acc_id, 'has_account', data.get('confidence', 0.7))
        
        email_info = findings.get('email_info', {})
        if email_info.get('email'):
            email_id = f'email_{email_info["email"]}'
            self.add_email(email_id, email_info['email'])
            self.add_connection(person_id, email_id, 'has_email', 0.9)
        
        phone_info = findings.get('phone_info', {})
        if phone_info.get('phone'):
            phone_id = f'phone_{phone_info["phone"]}'
            self.add_phone(phone_id, phone_info['phone'], phone_info.get('carrier', ''))
            self.add_connection(person_id, phone_id, 'has_phone', 0.85)
        
        breaches = findings.get('breaches', {})
        for key, data in breaches.items():
            if data.get('breaches_found', 0) > 0:
                self.add_connection(person_id, f'breach_{key}', 'found_in_breach', 0.8)
        
        return self.graph
    
    def export_neo4j(self) -> str:
        queries = []
        for node_id, node in self.graph['nodes'].items():
            if node['type'] == 'person':
                queries.append(f"CREATE (:{node['type']} {{id:'{node_id}', name:'{node['label']}', confidence:{node['confidence']}}})")
            elif node['type'] == 'account':
                queries.append(f"CREATE (:{node['type']} {{id:'{node_id}', platform:'{node['platform']}', username:'{node['username']}', url:'{node['url']}'}})")
        for edge in self.graph['edges']:
            queries.append(f"MATCH (a {{id:'{edge['source']}'}}), (b {{id:'{edge['target']}'}}) CREATE (a)-[:{edge['relationship']} {{confidence:{edge['confidence']}}}]->(b)")
        return '\n'.join(queries)
    
    def export_d3_json(self) -> dict:
        nodes = [{'id': nid, **ndata} for nid, ndata in self.graph['nodes'].items()]
        edges = self.graph['edges']
        return {'nodes': nodes, 'links': edges}
