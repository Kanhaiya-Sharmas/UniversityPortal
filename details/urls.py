from django.conf.urls import url
from details import views

urlpatterns = [
    url(r'^api/details$', views.details_list),
    url(r'^api/details/(?P<pk>[0-9]+)$', views.details_detail),
]
