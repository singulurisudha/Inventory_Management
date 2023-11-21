from django.urls import path
from user.views import (CustomUserRegistrationView , CustomUserLoginView, CustomUserRoleView,
                         CustomUserModuleView, CustomUserPermissionsView)
from django.urls import path


urlpatterns = [
    path('register/',CustomUserRegistrationView.as_view(),name='signup'),
    path('login/',CustomUserLoginView.as_view(),name='login'),
    path('login/refresh/',CustomUserLoginView.as_view(),name='refresh'),

    path('roles/', CustomUserRoleView.as_view(), name='role-list'),
    path('roles/<int:pk>/', CustomUserRoleView.as_view(), name='role-detail'),

    path('modules/', CustomUserModuleView.as_view(), name='module-list'),
    path('modules/<int:pk>/', CustomUserModuleView.as_view(), name='module-detail'),

    path('permissions/', CustomUserPermissionsView.as_view(), name='permissions-list'),

    path('custom_user_roles/', CustomUserRoleView.as_view(), name='custom_user_roles_list'),
    path('custom_user_roles/<int:pk>/', CustomUserRoleView.as_view(), name='custom_user_roles_detail'),

]