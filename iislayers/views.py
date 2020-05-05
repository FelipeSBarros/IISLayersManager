from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Layer

def index(request):
    return render(request, 'index.html')

def layers_list(request):
    template_name = 'layers_list.html'
    objects = Layer.objects.all()#'.only(
        #'scientificName', 'family', 'hasCoordinate',
        #'county', 'taxonRank', 'municipality', 'locality'
    #)
    paginator = Paginator(objects, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': objects,
        'page_obj': page_obj,
    }
    return render(request, template_name, context)
