# coding: utf-8
import json
from urllib.parse import urlencode

import requests
from rest_framework.reverse import reverse

from application_1.drivers.core_driver import conf


class RegistryDriver(object):

    @property
    def url(self):
        return conf.SERVER_SCHEME + '://' + conf.SERVER_NAME + ':' + conf.SERVER_PORT

    def get_reg_items(self, _filter=None):
        try:
            query_params = ''
            if _filter:
                query_params = '?' + urlencode(_filter)
            violations = json.loads(requests.get(self.url + reverse('registry-list') + query_params).text)
            return violations
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def get_reg_item(self, _pk=None):
        try:
            violation = json.loads(requests.get(self.url + reverse('registry-detail', kwargs={'pk': _pk})).text)
            return violation
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def create_reg_item(self):
        try:
            requests.post(self.url + reverse('registry-list'),
                          data={'json_data': '{"k1": 1, "k2": 2, "k3": 3}'})
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def update_reg_item(self, _pk):
        try:
            requests.put(self.url + reverse('registry-detail', kwargs={'pk': _pk}),
                         data={'violation': 'Нарушение 100', 'date': '2015-10-30', 'who': 'Петров 1'})
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def update_partial_reg_item(self, _pk):
        try:
            requests.patch(self.url + reverse('registry-detail', kwargs={'pk': _pk}),
                           data={'json_data': '{"k2": 33333}'})
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []
