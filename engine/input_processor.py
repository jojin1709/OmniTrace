import re
import hashlib
import uuid


class InputProcessor:
    @staticmethod
    def classify(input_data: dict) -> str:
        if 'photo' in input_data:
            return 'photo'
        if 'name' in input_data and ('email' in input_data or 'phone' in input_data or 'username' in input_data):
            return 'name'
        if 'email' in input_data:
            return 'email'
        if 'phone' in input_data:
            return 'phone'
        if 'username' in input_data:
            return 'username'
        if 'name' in input_data:
            return 'name'
        return 'unknown'

    @staticmethod
    def extract_leads(input_data: dict) -> dict:
        leads = {}
        for key in ['name', 'username', 'email', 'phone', 'photo']:
            if key in input_data and input_data[key]:
                leads[key] = input_data[key]
        return leads

    @staticmethod
    def build_target(input_data: dict) -> dict:
        target = {
            'inputs': list(input_data.keys()),
            'query': {k: v for k, v in input_data.items()},
        }
        if 'name' in input_data:
            parts = input_data['name'].split()
            target['name'] = input_data['name']
            target['first_name'] = parts[0] if parts else ''
            target['last_name'] = parts[-1] if parts else ''
        if 'email' in input_data:
            target['email'] = input_data['email']
            target['email_domain'] = input_data['email'].split('@')[-1]
        if 'phone' in input_data:
            target['phone'] = input_data['phone']
        if 'username' in input_data:
            target['username'] = input_data['username']
        return target
