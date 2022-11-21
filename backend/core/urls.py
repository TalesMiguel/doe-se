from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('add-acao/', views.add_acao, name='add acao'),
    path('get-acao/', views.get_acao, name='get acao'),
]