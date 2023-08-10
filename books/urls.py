from django.contrib import admin
from django.urls import path
from .views import BookListView

urlpatterns = [
    path("", BookListView.as_view(), name="home")

]
