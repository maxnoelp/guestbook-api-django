from django.urls import path
from . import views

urlpatterns = [
    path('guestbook/', views.content_list, name='content_list'),
    path('guestbook/<int:pk>/', views.content_detail , name="content_detail")
]
