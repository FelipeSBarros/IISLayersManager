from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

class Layer(models.Model):
    # about registration/modification
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.TextField(blank=True, null=True)#models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    observations = models.TextField(blank=True, null=True)

    # About layer registered
    layer_name = models.CharField(max_length=200)
    layer_type_choices = [
        ('vector file', 'vector file'),
        ('raster file', 'raster file')
    ]
    layer_type = models.CharField(
        max_length=12,
        choices=layer_type_choices,
        default='vector file',
    )
    '''layerExtension_choices = [
        ('.shp', '.shp'),
        ('.gpkg', '.gpkg'),
        (".tif", ".tif"),
        (".asc", ".asc"),
    ]
    layerExtension = models.CharField(
        max_length=10,
        choices=layerExtension_choices,
        default='.shp',
    )'''
    layer_resolution = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    layer_resolution_unit = models.CharField(
        max_length=15,
        choices=[
            ('Meters', 'm'),
            ('Kilometers', 'Km'),
            ('Decimal Degrees', 'Decimal Degrees'),
        ],
        default='m',
    )
    layer_crs = models.IntegerField(blank=True, null=True)
    layer_year_reference = models.CharField(max_length=200, blank=True, null=True)

    # About layer publication
    doi = models.CharField(max_length=200, blank=True, null=True)
    published_year = models.CharField(max_length=10, blank=True, null=True)
    paper_title = models.CharField(max_length=200, blank=True, null=True)
    paper_author = models.CharField(max_length=200, blank=True, null=True)
    paper_link = models.CharField(max_length=200, blank=True, null=True)
    paper_subject =  models.CharField(max_length=200, blank=True, null=True)
    paper_author_ORCID = models.URLField(blank=True, null=True)
    paper_year = models.TextField(blank=True, null=True)
    project_name = models.TextField(blank=True, null=True)

    # Layer link
    layer_url = models.URLField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    repository_url = models.URLField(blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        #self.modified_by = settings.AUTH_USER_MODEL
        self.save()

    def __str__(self):
        return self.layer_name

    def get_absolute_url(self):
        return reverse_lazy('iislayers:layer_details', kwargs={'pk': self.pk})
