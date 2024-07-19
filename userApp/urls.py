from django.urls import path
from .views import (
    index, SignupView, LoginView, UserListView, UserDetailView,
    UserUpdateView, UserDeleteView, UserByUsernameView, UserByEmailView,
    UserByPhoneView, UserByFirstNameView, UserByLastNameView, PasswordResetView,
    UpdateUsernameView, UserCountView, UserTrendView, UserDownloadPDFView, UserDownloadExcelView, LogoutView
)

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('find_user/username/<str:username>/', UserByUsernameView.as_view(), name='user-by-username'),
    path('find_user/email/<str:email>/', UserByEmailView.as_view(), name='user-by-email'),
    path('find_user/phone/<str:phone>/', UserByPhoneView.as_view(), name='user-by-phone'),
    path('find_user/firstname/<str:first_name>/', UserByFirstNameView.as_view(), name='user-by-firstname'),
    path('find_user/lastname/<str:last_name>/', UserByLastNameView.as_view(), name='user-by-lastname'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('update-username/', UpdateUsernameView.as_view(), name='update-username'),
    path('user-count/', UserCountView.as_view(), name='user-count'),
    path('user-trends/', UserTrendView.as_view(), name='user-trends'),
    path('users/download/pdf/', UserDownloadPDFView.as_view(), name='user-download-pdf'),
    path('users/download/excel/', UserDownloadExcelView.as_view(), name='user-download-excel'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
