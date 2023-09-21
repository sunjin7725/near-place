import os
import json

ROOT_DIR = os.path.abspath(os.path.join(__name__, os.pardir))
DATA_DIR = os.path.join(ROOT_DIR, 'data')

with open(os.path.join(ROOT_DIR, 'secrets.json'), 'r+') as f: 
    SECRET_CONFIG = json.load(f)