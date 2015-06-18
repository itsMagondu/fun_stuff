from rest_framework import routers

from logger.views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
