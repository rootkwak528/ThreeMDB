from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/review/', views.review_create),
    path('<int:movie_pk>/review/<int:review_pk>/delete/', views.review_delete),
]
