# # helloworld/urls.py
# from django.conf.urls import url
#
# from django.conf.urls.static import static
# from helloworld import views
#
# urlpatterns = [
#     url(r'^$', views.Home.as_view()),
#     url(r'^post_list.html$', views.HomePageView.as_view()),
# ]
from django.conf.urls import patterns, include, url
from helloworld.views import *

urlpatterns = patterns('',
    url(r'^search/', search),
    url(r'^index/', index)
)