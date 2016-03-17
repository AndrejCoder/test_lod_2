# coding: utf-8
import json

import requests
from rest_framework.reverse import reverse

from licenses.drivers.core_driver import conf


class ProcessDriver(object):

    @property
    def url(self):
        return conf.SERVER_SCHEME + '://' + conf.SERVER_NAME + ':' + conf.SERVER_PORT

    def get_processes(self, **kwargs):
        try:
            processes = json.loads(requests.get(self.url + reverse('processes')).content)
            return processes
        except ValueError:
            print u'Не правильный формат ответа от сервиса'
            return []
        except requests.ConnectionError:
            print u'Не удалось подключиться к серверу сервиса'
            return []
