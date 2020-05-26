from django import forms
from .models import Layer

class LayerForm(forms.ModelForm):
    doi = forms.CharField(required=False, label='e.g.: 10.1145/1067268.1067287')
    layer_year_reference = forms.CharField(required=False, label="e.g: 2000 or 2000 and 2001 or 2000-2001")
    layer_subject = forms.CharField(required=False, label="use comma (' , ') to separate subjects")


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
        'layer_subject',
        'observations',

        # About layer publication
        'doi',
        'project_name',

        # Layer link
        'layer_url',
        'project_url',
        'repository_url',
        )
