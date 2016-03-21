# coding: utf-8
from annoying.decorators import render_to

from licenses.drivers.core_driver.driver import ProcessDriver


@render_to('index.html')
def processes(request):
    pd = ProcessDriver()
    if request.GET and request.GET.get('create'):
        pd.create_process()
    ctx = {'processes': pd.get_processes(request.GET.dict()), 'process': pd.get_process(_pk=request.GET.get('id'))}
    return ctx
