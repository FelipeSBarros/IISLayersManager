from django.urls import path
from . import views as v

app_name = 'iislayers'

urlpatterns = [
    path('', v.index, name='index'),
    path('layerslist/', v.layer_list, name='list'),
    path('layer/<int:pk>', v.layer_details, name='layer_details'),
    path('layer/<int:pk>/edit/', v.edit_layer, name='edit_layer'),
    path('layer/new/', v.add_layer, name='new_layer'),
    path('layer/<pk>/remove/confirmation/', v.remove_confirmation, name='remove_confirmation'),
    path('layer/<pk>/remove/', v.remove_layer, name='remove_layer'),
]
