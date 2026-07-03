import yaml
import os


class Config:
    _config = None
    _keys = None

    @classmethod
    def load(cls):
        if cls._config is None:
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cfg_path = os.path.join(base, 'config.yaml')
            if os.path.exists(cfg_path):
                with open(cfg_path, 'r') as f:
                    cls._config = yaml.safe_load(f) or {}
            else:
                cls._config = {}
        return cls._config

    @classmethod
    def load_keys(cls):
        if cls._keys is None:
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            cfg = cls.load()
            keys_file = cfg.get('keys_file', 'config/keys.yaml')
            keys_path = os.path.join(base, keys_file)
            if not os.path.exists(keys_path):
                example_path = os.path.join(base, 'config', 'keys.example.yaml')
                if os.path.exists(example_path):
                    keys_path = example_path
                else:
                    cls._keys = {}
                    return cls._keys
            try:
                with open(keys_path, 'r') as f:
                    raw = yaml.safe_load(f) or {}
                cls._keys = raw.get('services', {})
            except Exception:
                cls._keys = {}
        return cls._keys

    @classmethod
    def get(cls, key, default=None):
        cfg = cls.load()
        return cfg.get(key, default)

    @classmethod
    def get_key(cls, service, key, default=None):
        keys = cls.load_keys()
        svc = keys.get(service, {})
        return svc.get(key, default)

    @classmethod
    def is_enabled(cls, service):
        keys = cls.load_keys()
        svc = keys.get(service, {})
        return bool(svc.get('enabled', False))
