from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.home, name="signup"),
    url(r'^login/$', views.home, name="login"),
    url(r'^logout/$', views.home, name="logout"),
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^profile/$', views.profile, name='profile'),
]
