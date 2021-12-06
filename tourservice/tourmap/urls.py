from django.urls import path
import tourmap.views

urlpatterns = [
    path('map_test1/', tourmap.views.map_test1, name='map_test1'),
]