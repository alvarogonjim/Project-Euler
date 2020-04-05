#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Decorator to measure the execution time of a method
"""

import time

__author__ = "Álvaro González Jiménez"
__license__ = "MIT"
__maintainer__ = "Álvaro González Jiménez"
__email__ = "alvaro.gonzalez-jimenez@inria.fr"


def timeit(method):
    """
    @timeit decorator which allows you to measure the execution time of the
    method/function by just adding the @timeit decorator on the method.
    :param method: Method/Function you want to measure
    :return: Execution time
    """

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
        return result

    return timed
