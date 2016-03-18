from rest_framework.routers import SimpleRouter

from core.api import ProcessViewset, ProcessTypeViewset

# urlpatterns = [
#     url(r'^api/get/processes/$', ProcessViewset.as_view({'get': 'list'}), name='processes'),
#     url(r'^api/get/process/(?P<pk>[0-9]+)/$', ProcessViewset.as_view({'get': 'retreave'}), name='process'),
#
#     url(r'^api/get/process_types/$', ProcessTypeViewset.as_view({'get': 'list'}), name='process_types'),
#     url(r'^api/get/process_type/(?P<pk>[0-9]+)/$', ProcessTypeViewset.as_view({'get': 'get'}), name='process_type')
# ]

router = SimpleRouter()
router.register(r'processes', ProcessViewset, 'process')
router.register(r'process_types', ProcessTypeViewset, 'process_type')

urlpatterns = router.urls

