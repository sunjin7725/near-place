import os
import sqlite3

from config import DATA_DIR


class PlaceDB:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PlaceDB, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, ) -> None:
        self.conn = sqlite3.connect(os.path.join(DATA_DIR, 'place.db'))