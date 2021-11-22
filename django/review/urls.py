from django.urls import path
from . import views

app_name = 'review'
urlpatterns = [
    path('', views.review_list_or_create, name='review_list_or_create'),
    path('<int:review_pk>/', views.review_detail_or_update_or_delete, name='review_detail_or_update_or_delete'),
]