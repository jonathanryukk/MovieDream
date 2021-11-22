from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('detail/<int:movie_pk>/', views.movie_detail),
    path('detail/<int:movie_id>/rank_list_create/', views.rank_list_or_create),
    path('detail/<int:rank_pk>/rank_delete/', views.rank_delete),
    path('detail/<int:movie_pk>/rank_update/', views.rank_update),
]
