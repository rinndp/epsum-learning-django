from django.urls import path, include
from users.views import CheckStatusView, AllUsersView, GetUserByEmailView, GetUserByRoleView, GetUserByRoleSlugView, \
    RegisterUserView

urlpatterns = [
    path('v1/check-status', CheckStatusView.as_view(), name='check-status'),
    path('v1/users', AllUsersView.as_view(), name='get-users'),
    path('v1/users/get-by-email', GetUserByEmailView.as_view(), name='get-user-by-email'),
    path('v1/users/get-by-role', GetUserByRoleView.as_view(), name='get-users-by-role'),
    path('v1/users/get-by-role-slug/<slug:slug>', GetUserByRoleSlugView.as_view(), name='get-users-by-role-slug'),
    path('v1/users/register', RegisterUserView.as_view(), name='register'),
]
