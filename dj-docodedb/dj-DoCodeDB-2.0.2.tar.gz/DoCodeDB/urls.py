from django.urls import path

from . import views

urlpatterns = [
    # Vistas AJAX
    path('modaleditar/', views.modaleditar, name='modaleditar'),
    # Vistas AJAX
]