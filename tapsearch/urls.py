from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.startpage, name='welcome'),
    url(r'^index/',views.indexView,name='index'),
    url(r'^submitted/',views.InputTextView),
    url(r'^search/',views.searchView),
    url(r'^results/',views.search),
    url(r'^clear/',views.clear)


]