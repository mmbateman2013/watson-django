from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Environment, Collection
from .forms import QueryForm


def query(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            results = form.query_environ()
            query = form.queryText
            return render(request, 'environment/results.html', {'query':query,'results':results})
    else:
        form = QueryForm()
    return render(request, 'environment/query.html', {'form':form})
    

def index(request):
    all_environs = Environment.objects.all()
    return render(request, 'environment/index.html', {'all_environs': all_environs,})

def env_detail(request, environment_id):
    environ = get_object_or_404(Environment, pk=environment_id)
    return render(request, 'environment/env_detail.html', {'environ': environ,})
    
#NOT CURRENTLY in URLS TODO
def col_documents(request, environment_id ,collection_id):
    environ = get_object_or_404(Environment, pk=environment_id)
    collect = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'environment/documents.html', {'environ': environ,'collect': collect})
    
#TODO: Add view for adding collections
#TODO: Add view for adding documents to a collection
#TODO: Add view to call forms.py QueryForm and hook up Michael's html and css
#TODO: Add view to display results of QueryForm after API is called