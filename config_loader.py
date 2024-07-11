import json
from types import SimpleNamespace

def dict_to_namespace(d):
    if isinstance(d, dict):
        for key, value in d.items():
            d[key] = dict_to_namespace(value)
        return SimpleNamespace(**d)
    elif isinstance(d, list):
        return [dict_to_namespace(item) for item in d]
    else:
        return d

def load_config(config_file):
    with open(config_file) as f:
        config_dict = json.load(f)
    return dict_to_namespace(config_dict)
