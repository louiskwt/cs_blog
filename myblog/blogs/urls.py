from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # post views
    path("", views.post_list, name="home"),
]