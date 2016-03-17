from django.conf.urls import url

from core.api import ProcessList, ProcessDetail

urlpatterns = [
    url(r'^api/get/processes/$', ProcessList.as_view(), name='processes'),
    url(r'^api/get/process/(?P<pk>[0-9]+)/$', ProcessDetail.as_view(), name='process'),
]
