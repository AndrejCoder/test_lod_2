# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.shortcuts import render

from application_1.drivers.core_driver.driver import RegistryDriver


def index(request):
    template_name = "index.html"
    return render(request, template_name)


@render_to('index.html')
def processes(request):
    pd = RegistryDriver()
    if request.GET and request.GET.get('create'):
        pd.create_reg_item()

    if request.GET and request.GET.get('update'):
        pd.update_reg_item(4)

    if request.GET and request.GET.get('update_patch'):
        pd.update_partial_reg_item(9)
    ctx = {'reg_items': pd.get_reg_items(request.GET.dict()), 'reg_item': pd.get_reg_item(_pk=request.GET.get('id'))}
    return ctx
