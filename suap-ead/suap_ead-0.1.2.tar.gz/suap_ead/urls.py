from django.urls import path
from .views import LoginView, CompleteView, redirect_to_login, redirect_to_logout

app_name = 'suap_ead'

urlpatterns = [
    path('jwt/login/', LoginView.as_view(), name='login'),
    path('jwt/complete/', CompleteView.as_view(), name='complete'),
    path('admin/login/', redirect_to_login, name='redirect_to_login'),
    path('admin/logout/', redirect_to_logout, name='redirect_to_logout'),
]
