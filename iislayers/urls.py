from django.urls import path
from . import views as v

app_name = 'iislayers'

urlpatterns = [
    path('', v.index, name='index'),
    path('layerslist/', v.layers_list, name='list'),
]