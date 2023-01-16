from django.urls import path

from . import views

urlpatterns = [
    path('add-acao/', views.add_acao, name='add acao'),
    path('get-acao/', views.get_acao, name='get acao'),
    path('edit-acao/', views.update_acao, name='edit acao'),
    path('delete-acao/', views.delete_acao, name='delete acao'),
    path('add-instituicao/', views.create_instituicao, name='create instituicao'),
    path('list-instituicao/', views.list_instituicao, name='list instituicao'),
    path('edit-instituicao/', views.update_instituicao, name='update instituicao'),
    path('delete-instituicao/', views.delete_instituicao, name='delete instituicao'),
    path('get-geojson/', views.get_geojson, name='get geojson'),
    path('get-coord/', views.get_coord, name='get coord'),
]
