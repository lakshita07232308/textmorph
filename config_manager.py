# config_manager.py
import yaml
import os

class ConfigManager:
    def __init__(self, config_path="config.yaml"):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self, *keys, default=None):
        """Access nested config values using keys, e.g., get('models', 'abstractive')"""
        value = self.config
        try:
            for key in keys:
                value = value[key]
            return value
        except KeyError:
            return default
