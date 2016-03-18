# coding: utf-8
import json
from urllib import urlencode

import requests
from rest_framework.reverse import reverse

from licenses.drivers.core_driver import conf


class ProcessDriver(object):

    @property
    def url(self):
        return conf.SERVER_SCHEME + '://' + conf.SERVER_NAME + ':' + conf.SERVER_PORT

    def get_processes(self, _filter=None, **kwargs):
        try:
            query_params = ''
            if _filter:
                query_params = '?' + urlencode(_filter)
            processes = json.loads(requests.get(self.url + reverse('process-list') + query_params).text)
            return processes
        except ValueError:
            print u'Неправильный формат ответа от сервиса'
            return []
        except requests.ConnectionError:
            print u'Не удалось подключиться к серверу сервиса'
            return []

    def get_process(self, _pk=None, **kwargs):
        try:
            processes = json.loads(requests.get(self.url + reverse('process-detail', kwargs={'pk': _pk})).text)
            return processes
        except ValueError:
            print u'Неправильный формат ответа от сервиса'
            return []
        except requests.ConnectionError:
            print u'Не удалось подключиться к серверу сервиса'
            return []

