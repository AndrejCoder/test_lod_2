from rest_framework.routers import SimpleRouter

from reqs.api import RequestViewset, ActivityPlaceViewset

router = SimpleRouter()
router.register(r'request', RequestViewset, 'request')
router.register(r'activity-place', ActivityPlaceViewset, 'activity-place')

urlpatterns = router.urls
