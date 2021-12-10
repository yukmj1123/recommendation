from django.urls import path
from mainpage import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #*path('', views.index, name='index'),
    path('', views.mainpage, name='mainpage'),
    path('new/', views.new),
    path('third/', views.third),
    path('list',views.listFunc)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)