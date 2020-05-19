from django import forms
from .models import Layer

class LayerForm(forms.ModelForm):

    class Meta:
        model = Layer
        fields = (
            # About Layer
        'layer_name',
        'layer_type',
        'layer_resolution',
        'layer_resolution_unit',
        'layer_crs',
        'layer_year_reference',

        # About layer publication
        'doi',
        'project_name',

        # Layer link
        'layer_url',
        'project_url',
        'repository_url',
        )
