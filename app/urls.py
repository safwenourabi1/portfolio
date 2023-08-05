

from django.urls import path,re_path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path("main", views.main, name="main"),
    path('main/RepairTicketProject', views.show1, name='main/RepairTicketProject'),
    path("main/databaseprojectmanagment", views.show2, name="main/databaseprojectmanagment"),
    path("main/imageencryption", views.show3, name="main/imageencryption"),
    path("main/electronicproject", views.show4, name="main/electronicproject"),
    path("", views.redir, name=""),
    re_path(r'^.*$', views.handle_nonexistent_url, name='catch-all'),

]
