from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.timeline),
    url(r'^timeline/$', views.timeline),
    url(r'^profile/$', views.profile),
    # url(r'^$', views.homepage),
]
