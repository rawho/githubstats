from django.urls import path
from . import views

urlpatterns = [
    path("user/<str:username>", views.user_details, name='user_details'),
    path("search", views.search, name="search"),
    path("", views.index, name="index")

]