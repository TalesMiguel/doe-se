from django.urls import path

from . import views

urlpatterns = [
    path('add-acao/', views.add_acao, name='add acao'),
    path('get-acao/', views.get_acao, name='get acao'),
    path('get-geojson/', views.get_geojson, name='get geojson'),
    path('get-coord/', views.get_coord, name='get coord'),
]
