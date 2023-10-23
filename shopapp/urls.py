from django.urls import path, re_path
from . import views
from .views import MyDataAPIView

urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path('api/mydata/', MyDataAPIView.as_view(), name='mydata-api'),
]