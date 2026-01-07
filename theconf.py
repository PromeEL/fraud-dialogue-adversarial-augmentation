import argparse
import yaml
import sys

class Config:
    _instance = None
    conf = {}

    def __init__(self, config_file=None):
        if config_file:
            # handle cases where file might not exist or be relative
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    self.conf = yaml.safe_load(f)
            except Exception as e:
                print(f"Error loading config file {config_file}: {e}")
                self.conf = {}
        Config._instance = self

    @staticmethod
    def get():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    def __getitem__(self, item):
        return self.conf[item]

    def __setitem__(self, key, value):
        self.conf[key] = value

    def __contains__(self, key):
        return key in self.conf

class ConfigArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        if 'conflict_handler' in kwargs:
            kwargs.pop('conflict_handler') # argparse might support it but let's be safe or pass it
        super().__init__(*args, **kwargs)
        self.add_argument('-c', '--config', help='config file path')

    def parse_args(self, args=None, namespace=None):
        args = super().parse_args(args, namespace)
        if hasattr(args, 'config') and args.config:
            # print(f"Loading config from {args.config}")
            Config(args.config)
        return args
