from django.conf.urls import url
from details import views

urlpatterns = [
    url(r'^api/superuser$', views.mentor_full),
    url(r'^api/superuser$', views.student_full),
    url(r'^api/superuser/(?P<pk>[0-9]+)$', views.mentor_byid),

    url(r'^api/mentor$', views.list_menortor),
    url(r'^api/mentor$$', views.student_list),
    url(r'^api/mentor/(?P<pk>[0-9]+)$', views.mentor_detail),



]
