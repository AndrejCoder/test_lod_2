from rest_framework.routers import SimpleRouter

from registries.api import RegistryViewset, ActivityPlaceViewset


router = SimpleRouter()
router.register(r'registry', RegistryViewset, 'registry')
router.register(r'ap', ActivityPlaceViewset, 'ap')

urlpatterns = router.urls
