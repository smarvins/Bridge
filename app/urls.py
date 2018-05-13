from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.timeline, name='timeline'),
    url(r'^search/$', views.search, name='search'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^profile/$', views.profile, name='profile'),
    # url(r'^$', views.homepage),
]
