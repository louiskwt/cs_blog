from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    # post views
    path("", views.post_list, name="home"),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),
]