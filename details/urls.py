from django.conf.urls import url
from details import views

urlpatterns = [
    # Superuser can "list, add, delete" all the Mentors and Students,
    url(r'^api/superuser$', views.mentor_full),
    url(r'^api/superuser/(?P<pk>[0-9]+)$', views.mentor_byid),
    url(r'^api/superuser/student', views.student_full),

    # Mentors can "list, add, delete" all the Students
    url(r'^api/mentor$', views.student_only),
    url(r'^api/mentor/(?P<pk>[0-9]+)$', views.student_onlybyid),

    # Students can only "list" all the Students details and details by id
    url(r'^api/student$', views.student_list),
    url(r'^api/student/(?P<pk>[0-9]+)$', views.student_listbyid),
]
