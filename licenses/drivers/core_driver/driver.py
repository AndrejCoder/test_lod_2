# coding: utf-8
import json
from urllib.parse import urlencode

import requests
from rest_framework.reverse import reverse

from licenses.drivers.core_driver import conf


class RegistryDriver(object):

    @property
    def url(self):
        return conf.SERVER_SCHEME + '://' + conf.SERVER_NAME + ':' + conf.SERVER_PORT

    def get_violations(self, _filter=None):
        try:
            query_params = ''
            if _filter:
                query_params = '?' + urlencode(_filter)
            violations = json.loads(requests.get(self.url + reverse('violation-list') + query_params).text)
            return violations
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def get_violation(self, _pk=None):
        try:
            violation = json.loads(requests.get(self.url + reverse('violation-detail', kwargs={'pk': _pk})).text)
            return violation
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def create_violation(self):
        try:
            requests.post(self.url + reverse('violation-list'),
                          data={'violation': 'Нарушение 100', 'date': '2015-10-30', 'who': 'Петров 1'})
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def update_violation(self, _pk):
        try:
            requests.put(self.url + reverse('violation-detail', kwargs={'pk': _pk}),
                         data={'violation': 'Нарушение 100', 'date': '2015-10-30', 'who': 'Петров 1'})
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []

    def update_partial_violation(self, _pk):
        try:
            requests.patch(self.url + reverse('violation-detail', kwargs={'pk': _pk}),
                           data={'violation': 'Нарушение 007'})
        except ValueError:
            print(u'Неправильный формат ответа от сервиса')
            return []
        except requests.ConnectionError:
            print(u'Не удалось подключиться к серверу сервиса')
            return []
