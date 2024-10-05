from django.urls import path
from .views import get_weather

urlpatterns = [
    path('weather/<str:lat>/<str:lon>/', get_weather),

]
