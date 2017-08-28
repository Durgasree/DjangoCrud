from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from students import views

urlpatterns = [
  url(r'^$', views.AllStudents.as_view(),name='all_students'),
  url(r'^new$', views.StudentCreate.as_view(), name='student_new'),
  url(r'^edit/(?P<pk>\d+)$', views.StudentUpdate.as_view(), name='student_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.StudentDelete.as_view(), name='student_delete'),
]