
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_user, name='register'),
    
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # path('password-reste/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reste/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reste/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reste/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/<email>/', views.user_detail, name='user_detail'),
    
]
