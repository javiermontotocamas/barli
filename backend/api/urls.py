from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index, name="index"),
    path('get_users', views.get_users, name='get_users'),
    path('get_users_by_id/<int:user_id>/', views.get_user_by_id, name='get_users'),
]
