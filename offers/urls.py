from django.conf.urls import url
from . import views

app_name = 'offers'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ofertas/(?P<job_id>[0-9]+)/$', views.show, name='show'),
    url(r'^login/$', views.login, name='login'),
]
