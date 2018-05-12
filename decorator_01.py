# -*- coding: utf-8 -*-

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time,functools

def metric(fn):
    print('%s excuted in %s ms' % (fn.__name__, 10.24))
