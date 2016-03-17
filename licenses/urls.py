from django.conf.urls import url

from licenses.api import LicenseList, LicenseDetail

urlpatterns = [
    url(r'^api/license_list/$', LicenseList.as_view(), name='licenses_list'),
    url(r'^api/license/(?P<pk>[0-9]+)/$', LicenseDetail.as_view(), name='license_detail'),
]
