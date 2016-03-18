# coding: utf-8
from annoying.decorators import render_to

from licenses.drivers.core_driver.driver import ProcessDriver


@render_to('index.html')
def processes(request):
    pd = ProcessDriver()
    ctx = {'processes': pd.get_processes(request.GET.dict())}
    return ctx
