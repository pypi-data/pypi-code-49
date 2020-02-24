from rest_framework.routers import DefaultRouter

from huscy.rooms import views


router = DefaultRouter()
router.register('buildings', views.BuildingViewSet)
router.register('floors', views.FloorViewSet)
router.register('rooms', views.RoomViewSet)
