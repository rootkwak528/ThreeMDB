from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_create),
    # path('<int:movie_pk>/', views.movie_detail),
]
