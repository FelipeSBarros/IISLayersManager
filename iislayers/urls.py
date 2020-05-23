from django.urls import path
from . import views as v

app_name = 'iislayers'

urlpatterns = [
    path('', v.index, name='index'),
    path('layerslist/', v.layer_list, name='list'),
    path('layer/<int:pk>', v.layer_details, name='layer_details'),
    path('layer/<int:pk>/edit/', v.edit_layer, name='edit_layer'),
    path('layer/new/', v.add_layer, name='new_layer'),
]
