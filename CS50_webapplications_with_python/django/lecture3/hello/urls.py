from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("brian1", views.brian, name="brian")
]