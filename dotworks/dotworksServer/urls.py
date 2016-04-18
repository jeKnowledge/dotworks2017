from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='student_register'),
    url(r'^register/$', views.student_register, name='register'),
    url(r'^register_action/$', views.register_action, name='register_action'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^create_internship$', views.internship_creation, name = 'internship_creation'),
    url(r'^internship_creation_action$', views.internship_creation_action,
        name = 'internship_creation_action'),
    url(r'^internship/(?P<internship_id>[0-9]+)/$', views.internship_details, 
        name = 'internship_details'),
    url(r'^company_area$', views.company_area, name = "company_area"),
    url(r'^internship_addition/(?P<internship_id>[0-9]+)/$', views.inscription_addition,
        name = 'inscription_addition'),
    url(r'^inscription_add_action/(?P<internship_id>[0-9]+)/$', views.inscription_add_action,
        name = 'inscription_add_action'),
]