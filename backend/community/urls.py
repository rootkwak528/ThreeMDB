from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/review/', views.review_create),
    path('review/<int:review_pk>/', views.review_delete_update),
    path('review/<int:review_pk>/comment/', views.comment_create),
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_delete_update),
]
