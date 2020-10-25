from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_detail, name="bookmark_detail"),
    path("add/<str:repo_id>", views.bookmark_add, name="bookmark_add"),
    path("remove/<str:repo_id>", views.bookmark_remove, name="bookmark_remove")
]