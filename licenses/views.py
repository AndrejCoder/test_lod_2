# coding: utf-8
import json

import requests
from annoying.decorators import render_to


@render_to('index.html')
def process_list(request):
    ctx = {}
    try:
        processes = json.loads(requests.get('http://localhost:8000/core/api/process_list/').content)
        ctx = {'processes': processes}
    except ValueError:
        print u'Не правильный формат ответа от сервиса'
    except requests.ConnectionError:
        print u'Не удалось подключиться к серверу сервиса'

    return ctx
