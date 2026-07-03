"""
OmniTrace Pipeline Orchestrator
Takes ANY input type → runs ALL applicable modules → produces dossier
"""

from face.module import FaceModule
from image.module import ImageModule
from name.module import NameModule
from social.module import SocialModule
from username.module import UsernameModule
from email_intel.module import EmailModule
from phone.module import PhoneModule
from location.module import LocationModule
from network.module import NetworkModule
from breach.module import BreachModule
from document.module import DocumentModule
from darkweb.module import DarkWebModule
from crypto.module import CryptoModule
from engine.correlation.module import CorrelationEngine
from engine.input_processor import InputProcessor
from engine.report_generator import Dossier, ReportGenerator


class OmniTraceOrchestrator:
    def __init__(self):
        self.modules = {
            'face': FaceModule(),
            'image': ImageModule(),
            'name': NameModule(),
            'social': SocialModule(),
            'username': UsernameModule(),
            'email': EmailModule(),
            'phone': PhoneModule(),
            'location': LocationModule(),
            'network': NetworkModule(),
            'breach': BreachModule(),
            'document': DocumentModule(),
            'darkweb': DarkWebModule(),
            'crypto': CryptoModule(),
            'correlation': CorrelationEngine(),
        }
    
    def trace(self, input_data: dict) -> Dossier:
        input_type = InputProcessor.classify(input_data)
        leads = InputProcessor.extract_leads(input_data)
        target = InputProcessor.build_target(input_data)
        findings = {}
        
        if input_type in ('face', 'photo', 'place_photo'):
            if input_type in ('face', 'photo'):
                findings['face_matches'] = self.modules['face'].search(leads.get('image', ''))
            findings['reverse_image'] = self.modules['image'].reverse_search(leads.get('image', ''))
            findings['exif'] = self.modules['image'].extract_exif(leads.get('image', ''))
            findings['ocr'] = self.modules['image'].ocr(leads.get('image', ''))
            findings['objects'] = self.modules['image'].detect_objects(leads.get('image', ''))
            if input_type == 'place_photo':
                findings['place'] = self.modules['location'].identify_place(leads.get('image', ''))
        
        if input_type in ('name', 'username', 'email', 'phone'):
            if input_type == 'name':
                findings['people_search'] = self.modules['name'].search(leads.get('name', ''))
            if 'username' in leads:
                findings['username_matches'] = self.modules['username'].check(leads.get('username', ''))
            if 'email' in leads:
                findings['email_info'] = self.modules['email'].investigate(leads.get('email', ''))
            if 'phone' in leads:
                findings['phone_info'] = self.modules['phone'].lookup(leads.get('phone', ''))
            findings['social'] = self.modules['social'].search_all(leads)
            findings['breaches'] = self.modules['breach'].search(leads)
            findings['darkweb'] = self.modules['darkweb'].search(leads)
        
        graph_data = self.modules['correlation'].build_graph(findings, target)
        confidence = self.modules['correlation'].score_confidence(findings, graph_data)
        dossier = ReportGenerator.build_dossier(target, findings, graph_data, confidence)
        return dossier
