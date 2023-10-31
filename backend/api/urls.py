from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get_users', views.get_users, name='get_users'),
    path('get_users_by_id/<int:user_id>/', views.get_user_by_id, name='get_users'),
]

