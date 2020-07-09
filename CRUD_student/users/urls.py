from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include
from .import views
from .views import UserPasswordChangeView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.StudentSignUpView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<str:pk>', views.StudentProfileView.as_view(), name='profile'),
    path('studentPorfileUpdate/<str:pk>', views.UpdateStudentProfileView.as_view(), name='updateStudent'),

    path('password_change/<str:pk>', UserPasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done', UserPasswordChangeDoneView.as_view(), name='password_change_done'),



    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_sent/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
