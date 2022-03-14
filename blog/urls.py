from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^api/article/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
        url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^blank_feedback/$', views.blank_feedback, name='blank_feedback'),
]
