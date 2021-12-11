from django.urls import path
from mainpage import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #*path('', views.index, name='index'),
    #path('mainpage/', views.mainpage),
    path('', views.new),
    path('third/', views.third),
    path('mainpage/',views.SearchFuncOk)



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)