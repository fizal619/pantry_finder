import logging
import os
import json


SETTINGS = {}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PATHS_TO_CONF = [
    os.path.join(BASE_DIR, 'conf', 'local_settings.json'),
    os.path.join(BASE_DIR, 'conf', 'settings.json')
]


# for each possible path, try to open the file
# if you can open the file, make it your settings file
for path in PATHS_TO_CONF:
    filename = path
    try:
        file_content = open(filename, 'r')
    except IOError:
        logging.error('File could not be found: {}'.format(filename))
    try:
        SETTINGS = json.loads(file_content.read())
    except ValueError:
        logging.error('No JSON object could be decoded.')
    if SETTINGS:
        break

def get(key):
    return SETTINGS.get(key, None)
