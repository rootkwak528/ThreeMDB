from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/review/', views.review_create),
]
