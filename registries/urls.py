from rest_framework.routers import SimpleRouter

from registries.api import ViolationRegistryViewset

router = SimpleRouter()
router.register(r'violations', ViolationRegistryViewset, 'violation')

urlpatterns = router.urls

