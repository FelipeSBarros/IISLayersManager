from django.conf import settings
from django.db import models
from django.utils import timezone

class Layer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    layerName = models.CharField(max_length=200)
    layerType_choices = [
        ('vector file', 'vector file'),
        ('raster file', 'raster file')
    ]
    layerType = models.CharField(
        max_length=12,
        choices=layerType_choices,
        default='vector file',
    )
    layerExtension_choices = [
        ('.shp', '.shp'),
        ('.gpkg', '.gpkg'),
        (".tif", ".tif"),
        (".asc", ".asc"),
    ]
    layerExtension = models.CharField(
        max_length=10,
        choices=layerExtension_choices,
        default='.shp',
    )
    layerResolution = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    publishedYear = models.CharField(max_length=200, blank=True, null=True)
    crs = models.CharField(max_length=200, blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    layerUrl = models.CharField(max_length=200, blank=True, null=True)
    projectUrl = models.CharField(max_length=200, blank=True, null=True)
    repositoryUrl = models.CharField(max_length=200, blank=True, null=True)
    doi = models.CharField(max_length=200, blank=True, null=True)

    def modify(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.layerName
