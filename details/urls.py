from django.conf.urls import url
from details import views

urlpatterns = [
    url(r'^api/superuser$', views.mentor_full),
    url(r'^api/superuser/student', views.student_full),
    url(r'^api/superuser/(?P<pk>[0-9]+)$', views.mentor_byid),
    url(r'^api/superuser/student', views.student_byid),

    url(r'^api/mentor$', views.student_only),
    url(r'^api/mentor/(?P<pk>[0-9]+)$', views.student_onlybyid),

]
