from rest_framework.routers import SimpleRouter

from registries.api import RegistryViewset

router = SimpleRouter()
router.register(r'registry', RegistryViewset, 'registry')

urlpatterns = router.urls

