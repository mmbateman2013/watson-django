from django.conf.urls import url
from . import views

app_name = 'environment'

urlpatterns = [
    # /environment/
    url(r'^$', views.index, name='index'),    
    
    # /environment/{id}/
    url(r'^(?P<environment_id>[0-9]+)/$', views.env_detail, name='env_detail'),
    
    # /environment/{environ_id}/collection/{collect_id}
    url(r'^(?P<environment_id>[0-9]+)/(?P<collection_id>[0-9]+)$', views.col_documents, name='documents'),
    
    # /environment/{environ_id}/query
    url(r'^(?P<environment_id>[0-9]+)/query$', views.query, name='query'),
    
    # /environment/{environ_id}/query/results
    url(r'^(?P<environment_id>[0-9]+)/query/results$', views.query, name='results'),
    
    # ex: /environment/contacts/
    url(r'^contacts/', views.contacts, name='contacts'),
    
    # /environment/{environ_id}/document/{doc_id}/detail
    url(r'^(?P<environment_id>[0-9]+)/document/(?P<document_id>[0-9]+)/detail$', views.document_detail, name='detail'),

    #TODO: Add views.col_documents
    #TODO: Add view for adding documents to a collection
    #TODO: Add view to call forms.py QueryForm and hook up Michael's html and css
    #TODO: Add view to display results of QueryForm after API is called
]