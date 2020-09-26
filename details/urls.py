from django.conf.urls import url
from details import views

urlpatterns = [
    url(r'^api/mentor$', views.mentor_list),

]
