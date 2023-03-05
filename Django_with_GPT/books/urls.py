from django.urls import path
from . import views

urlpatterns = [
   path('', views.book_list_or_create),
   path('<isbn>/', views.book_detail),
]