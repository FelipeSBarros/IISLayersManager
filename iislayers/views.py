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

@login_required
def layer_details(request, pk):
    template_name = 'layer_details.html'
    layer = Layer.objects.get(pk=pk)
    context = {
        'layer': layer,
    }
    return render(request, template_name, context)

@login_required
def add_layer(request):
    if request.method == "POST":
        form = OccForm(request.POST)
        if form.is_valid():
            occ = form.save(commit=False)
            occ.author = request.user
            # occ.published_date = timezone.now()
            occ.save()
            print("OK")
            template_name = 'occs_details.html'
            # occ = Occurrences_imibio.objects.get(pk=pk)
            context = {
                'occ_detail': occ,
            }
            return render(request, template_name, context)

    else:
        form = OccForm()
    return render(request, 'agregar_occ.html', {'form': form})
