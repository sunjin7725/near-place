import os
import json
import requests

from config import ROOT_DIR
from prj_class import Point2D

with open(os.path.join(ROOT_DIR, 'secrets.json'), 'r+') as f: 
    secret = json.load(f)

def search_local(query: str, display: int = None, start: int = None, sort: str = None) -> dict:    
    # 지역 검색 API
    url = 'https://openapi.naver.com/v1/search/local.json'

    header = {
        'X-Naver-Client-Id': secret.get('LOCAL_CLIENT_ID'),
        'X-Naver-Client-Secret': secret.get('LOCAL_CLIENT_SECRET'),
    }

    params = {
        'query': query,
        'display': display,
        'start': start,
        'sort': sort
    }
    
    request = requests.get(url, headers=header, params=params)
    return json.loads(request.text)


def addr_to_coord(query: str) -> Point2D:
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    
    header = {
        'X-NCP-APIGW-API-KEY-ID': secret.get('CLIENT_ID'),
        'X-NCP-APIGW-API-KEY': secret.get('CLIENT_SECRET'),
    }

    params = {
        'query': query
    }
    
    request = requests.get(url, headers=header, params=params)
    return json.loads(request.text)


def coord_to_addr(x: float, y: float) -> str:
    point = Point2D(x, y)
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    
    header = {
        'X-NCP-APIGW-API-KEY-ID': secret.get('CLIENT_ID'),
        'X-NCP-APIGW-API-KEY': secret.get('CLIENT_SECRET'),
    }

    params = {
        
    }
    
    request = requests.get(url, headers=header, params=params)
    return json.loads(request.text)


if __name__ == '__main__':
    print(addr_to_coord(query='대전광역시 서구 둔산동 959-2'))