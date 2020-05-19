from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Layer
from .forms import LayerForm

from doi_api import getPaperMetaData

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
        form = LayerForm(request.POST)
        if form.is_valid():
            layer = form.save(commit=False)
            # about registration/modification
            layer.registered_by = request.user
            layer.created_date = timezone.now()
            layer.modified_by = request.user
            if layer.doi is not None:

                # request paper metadata based on DOI
                paper_metadata_result = getPaperMetaData(layer.doi)

                # About layer publication
                layer.published_year = str(paper_metadata_result['paper_year'])
                layer.paper_title = paper_metadata_result['paper_title']
                layer.paper_author = paper_metadata_result['paper_author']
                layer.paper_author_ORCID = paper_metadata_result['paper_author_ORCID']
                layer.paper_link = paper_metadata_result['paper_link']
                layer.paper_subject = paper_metadata_result['paper_subject']

            layer.save()

            template_name = 'layer_details.html'
            #layer_added = Layer.objects.get(pk=pk)
            context = {
                'layer_detail': layer,
            }
            return render(request, template_name, context)

    else:
        form = LayerForm()
    return render(request, 'add_layer.html', {'form': form})
