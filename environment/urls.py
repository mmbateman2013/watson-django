from django.conf.urls import url
from . import views

app_name = 'environment'

urlpatterns = [
    # /environment/
    url(r'^$', views.index, name='index'),    
    
    # /environment/{id}/
    url(r'^(?P<environment_id>[0-9]+)/$', views.env_detail, name='env_detail'),
    
    # /environment/{environ_id}/collection/{collect_id}
    url(r'^(?P<environment_id>[0-9]+)/(?P<collection_id>[0-9]+)$', views.col_documents, name='documents')
]