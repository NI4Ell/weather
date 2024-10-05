import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

YANDEX_API_URL = "https://api.weather.yandex.ru/v2/forecast/"


@api_view(['GET'])
def get_weather(request, lat, lon):
    headers = {
        'X-Yandex-API-Key': settings.YANDEX_API_KEY
    }
    params = {
        'lat': lat,
        'lon': lon,
        'lang': 'ru_RU',
        'limit': 1
    }
    response = requests.get(YANDEX_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return Response(response.json())
    else:
        return Response({'error': 'Не удалось получить данные о погоде'}, status=response.status_code)
