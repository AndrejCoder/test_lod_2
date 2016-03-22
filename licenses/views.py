# coding: utf-8
from annoying.decorators import render_to

from licenses.drivers.core_driver.driver import RegistryDriver


@render_to('index.html')
def processes(request):
    pd = RegistryDriver()
    if request.GET and request.GET.get('create'):
        pd.create_violation()

    if request.GET and request.GET.get('update'):
        pd.update_violation(4)

    if request.GET and request.GET.get('update_patch'):
        pd.update_partial_violation(9)
    ctx = {'violations': pd.get_violations(request.GET.dict()), 'violation': pd.get_violation(_pk=request.GET.get('id'))}
    return ctx
