from django.conf.urls import url

from core.api import ProcessList, ProcessDetail

urlpatterns = [
    url(r'^api/process_list/$', ProcessList.as_view(), name='process_list'),
    url(r'^api/process/(?P<pk>[0-9]+)/$', ProcessDetail.as_view(), name='process_detail'),
]
