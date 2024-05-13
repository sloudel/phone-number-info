from django.urls import path

from phone_numbers.views import index, search, search_json


urlpatterns = [
    path('', index, name='phone_numbers'),
    path('search', search),
    path('search_json', search_json),
]
