from rest_framework.routers import SimpleRouter

from authentication.api import UserViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet, 'user')

urlpatterns = router.urls
