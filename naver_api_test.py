import os
import json
import requests

from config import ROOT_DIR, SECRET_CONFIG
from prj_class import Point2D

def search_local(query: str, display: int = None, start: int = None, sort: str = None) -> dict:    
    # 지역 검색 API
    url = 'https://openapi.naver.com/v1/search/local.json'

    header = {
        'X-Naver-Client-Id': SECRET_CONFIG.get('LOCAL_CLIENT_ID'),
        'X-Naver-Client-Secret': SECRET_CONFIG.get('LOCAL_CLIENT_SECRET'),
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
        'X-NCP-APIGW-API-KEY-ID': SECRET_CONFIG.get('CLIENT_ID'),
        'X-NCP-APIGW-API-KEY': SECRET_CONFIG.get('CLIENT_SECRET'),
    }

    params = {
        'query': query
    }
    
    request = requests.get(url, headers=header, params=params)
    return json.loads(request.text)


def coord_to_addr(x: float, y: float) -> str:
    point = Point2D(x, y)
    url = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
    
    header = {
        'X-NCP-APIGW-API-KEY-ID': SECRET_CONFIG.get('CLIENT_ID'),
        'X-NCP-APIGW-API-KEY': SECRET_CONFIG.get('CLIENT_SECRET'),
    }

    params = {
        'coords': f"{x},{y}",
        'output': 'json'
    }
    
    request = requests.get(url, headers=header, params=params)
    return json.loads(request.text)


if __name__ == '__main__':
    data = addr_to_coord(query='대전광역시 서구 둔산동 959-2')
    coord = Point2D(data.get('addresses')[0].get('x'), data.get('addresses')[0].get('y'))
    print(coord)
    address = coord_to_addr(coord.x, coord.y)
    print(address.get('results'))