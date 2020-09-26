from django.conf.urls import url
from details import views

urlpatterns = [
    url(r'^api/mentor$', views.mentor_list),
    url(r'^api/mentor/(?P<pk>[0-9]+)$', views.mentor_detail),
    url(r'^api/student$', views.student_list),


]
