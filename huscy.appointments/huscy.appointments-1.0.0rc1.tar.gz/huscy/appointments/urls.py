from rest_framework.routers import DefaultRouter

from huscy.appointments import views

router = DefaultRouter()
router.register('appointments', views.AppointmentsViewSet, basename='appointment')
router.register('resources', views.ResourcesViewSet)
