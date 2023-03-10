from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeForm,
    PasswordResetView, PasswordResetConfirmView
)

app_name = 'accounts'

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path("profile/", TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    # path("profile/edit/<pk>", views.ProfileEditView.as_view(),
    #      name='user_edit'),

    # path("accounts/user/<pk>", views.OtherProfileView.as_view(), name='profile_view'),

    # path("password/change/", PasswordChangeView.as_view(
    #     template_name='accounts/password_change.html',
    #     success_url="/",
    #     form_class=PasswordChangeForm), name='password_change'),


    # path("passoword/reset/", views.CustomPasswordReset.as_view(),
    #      name='password_reset'),

    # path("password/reset/confirm/<uidb64>/<token>/",
    #      PasswordResetConfirmView.as_view(
    #          template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm')
]