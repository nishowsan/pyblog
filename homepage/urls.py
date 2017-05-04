from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = 'home'

urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)$', DetailView.as_view(), name='details'),
    url(r'^about/$', AboutView.as_view(), name='about')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
