from django.conf import settings
from rest_framework.routers import SimpleRouter

from reqs.api import RequestViewset, JqGridRequestViewset

router = SimpleRouter()
router.register(r'request', RequestViewset, 'request')
if 'jqgrid_django_rest_framework' in settings.INSTALLED_APPS:
    router.register(r'jqgrid-request', JqGridRequestViewset, 'jqgrid-request')
# router.register(r'activity-place', ActivityPlaceViewset, 'activity-place')

urlpatterns = router.urls
