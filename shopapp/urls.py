from django.urls import path, re_path
from . import views
# from .views import MyDataAPIView
from .views import mydata_view

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path(r'^api/$', views.mydata_view, name='mydata-api'),
]