
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'articles', views.ArticleViewSet)
router.register(r'article_collections', views.ArticleCollectionViewSet)
router.register(r'imageassets', views.ImageAssetViewSet)
router.register(r'textassets', views.TextAssetViewSet)
router.register(r'richtextassets', views.RichTextAssetViewSet)

app_name = 'ripple'

urlpatterns = [

    # Account
    path('account/status', views.AccountStatusView.as_view()),
    path('account/log_in', views.LoginView.as_view(), name='log_in'),
    path('account/log_out', views.LogoutView.as_view()),
    path('account/sign_up', views.SignUpView.as_view()),
    path('account/<int:pk>/', views.UserUpdateView.as_view(), name="user_detail"),

    # Passwords
    path('account/password/reset', views.PasswordResetRequestView.as_view(),
         name='password_reset_request'),
    path('account/password/reset_confirm', views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('account/password/change', views.PasswordChangeView.as_view()),

    # Verification
    path('account/send_verify_email', views.SendEmailVerificationView.as_view()),
    path('account/verify_email',
         views.ConfirmEmailView.as_view(), name='verify_email'),

    # TODO red _ review these urls, are they needed?
    path('update_session_data', views.update_session_data),
    path('unpack_token', views.unpack_token),
    path('get_session_data', views.get_session_data),
    path('session', views.session),

    path('upload', views.simple_upload),
    path('assets', views.assets, name='assets'),
    path('assets_admin', staff_member_required(views.assets_admin)),

    path('', include(router.urls)),

]
