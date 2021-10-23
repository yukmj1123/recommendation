from django.urls import path
import tourmap.views

urlpatterns = [
    path('map_main/', tourmap.views.map_main, name='map_main'),
]