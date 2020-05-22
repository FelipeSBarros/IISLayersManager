from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView
from decimal import Decimal

from .models import Layer
from .forms import LayerForm

from doi_api import getPaperMetaData

def index(request):
    return render(request, 'index.html')

class LayersListView(ListView):
    paginate_by = 15
    template_name = 'layers_list.html'

    def get_queryset(self):
        qs = Layer.objects.all()
        q = self.request.GET.get('q')
        v = self.request.GET.get('v')

        if q == 'layer_name':
            qs = qs.filter(
                layer_name__icontains=v
            )
        if q == 'layer_resolution':
            v = Decimal(v.replace(',', '.'))
            qs = qs.filter(
                layer_resolution__icontains=v
            )
        if q == 'doi':
            qs = qs.filter(
                doi__icontains=v
            )
        if q == 'paper_subject':
            qs = qs.filter(
                paper_subject__icontains=v
            )

        return qs

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
                'layer': layer,
            }
            return render(request, template_name, context)

    else:
        form = LayerForm()
    return render(request, 'add_layer.html', {'form': form})

layer_list = LayersListView.as_view()
