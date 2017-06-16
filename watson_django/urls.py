from django.conf.urls import include , url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView 

urlpatterns = [
    url(r'^environment/', include('environment.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/environment/', permanent=True)), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)