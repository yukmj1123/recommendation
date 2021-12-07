from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #*path('', views.index, name='index'),
    path('', views.mainpage, name='mainpage'),
    path('new/', views.new),
    path('third/', views.third),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)