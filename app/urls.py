from .views import ListNews, CreateNews
from django.urls import path

urlpatterns = [
    path("", ListNews.as_view(), name="home"),
    path("create/", CreateNews.as_view(), name="create"),
]