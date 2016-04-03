import os
import json

settings_directory = os.path.dirname(os.path.realpath(__file__))
possible_paths = [
    os.path.join(settings_directory, 'setting.json'),
    os.path.join(settings_directory, 'default.json')
]

config = None

for file_path in possible_paths:
    if not os.path.isfile(file_path):
        continue

    with open(file_path, 'r') as f:
        file_data = f.read()
        config = json.loads(file_data)
        break

if not config:
    raise SystemError('Invalid or missing config file')

is_empty = lambda s: None if s == '' else s
config = {k: is_empty(config[k]) for k in config}


def get(key):
    return config[key]
