from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index, name="index"),
    path('register', views.RegisterView.as_view()),
    path('get_users', views.get_users, name='get_users'),
    path('get_users_by_id/<int:user_id>/', views.get_user_by_id, name='get_users'),
    path('bar', views.get_bars, name='get_bars'),
    path('bar/<int:id>/tables', views.process_tables_of_bar, name='process_tables_of_bar'),
    path('bar/<int:bar_id>/tables/<int:table_id>', views.delete_or_changue_table_of_bar, name='delete_or_changue_table_of_bar'),
    path('bar/<int:id>/ads', views.process_ads_of_bar, name='process_ads_of_bar'),
    path('bar/<int:bar_id>/ads/<int:ad_id>', views.delete_ad_of_bar, name='delete_ad_of_bar'),
    path('bar/<int:id>/data', views.process_data_of_bar, name='process_data_of_bar'),
    path('user/<int:id>/data', views.process_data_of_user, name='process_data_of_user'),
    path('user/<int:user_id>/booking/<int:table_id>', views.create_booking_by_user, name='create_booking_by_user'),
    path('user/<int:id>/booking', views.get_booking_by_user, name='get_booking_by_user'),
    path('bars', views.get_all_bars, name='get_all_bars'),
]
