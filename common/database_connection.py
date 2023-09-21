import os
import sqlite3
import psycopg2

from config import DATA_DIR, SECRET_CONFIG


class PostgresPlaceDB:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PostgresPlaceDB, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, ) -> None:
        self.conn = psycopg2.connect(host=SECRET_CONFIG.get('POSTGRESQL_HOST'), port=SECRET_CONFIG.get('POSTGRESQL_PORT'),
                                     user=SECRET_CONFIG.get('POSGGRESQL_USER'), password=SECRET_CONFIG.get('POSTGRESQL_PWD'),
                                     dbname='near_place')
                
        
class SQLitePlaceDB:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SQLitePlaceDB, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, ) -> None:
        self.conn = sqlite3.connect(os.path.join(DATA_DIR, 'place.db'))