from django.conf.urls import include, url
from feedback import views

urlpatterns = [

    url(r'^$', views.feedback, name='feedback'),
]
