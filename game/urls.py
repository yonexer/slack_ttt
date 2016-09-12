from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'slack_ttt'

urlpatterns = [
    url(r'^$', csrf_exempt(views.play)),
]