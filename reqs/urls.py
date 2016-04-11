from rest_framework.routers import SimpleRouter

from reqs.api import RequestViewset, JqGridRequestViewset

router = SimpleRouter()
router.register(r'request', RequestViewset, 'request')
router.register(r'jqgrid-request', JqGridRequestViewset, 'jqgrid-request')
# router.register(r'activity-place', ActivityPlaceViewset, 'activity-place')

urlpatterns = router.urls
