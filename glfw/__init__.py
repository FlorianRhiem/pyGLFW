"""
Python bindings for GLFW.
"""

__author__ = 'Florian Rhiem (florian.rhiem@gmail.com)'
__copyright__ = 'Copyright (c) 2013-2016 Florian Rhiem'
__license__ = 'MIT'
__version__ = '1.5.1'

# By default (ERROR_REPORTING = True), GLFW errors will be reported as Python
# exceptions. Set ERROR_REPORTING to False or set a curstom error callback to
# disable this behavior.
ERROR_REPORTING = True

from . import GLFW
import re

_globals = globals()

for name in dir(GLFW):
    if name.startswith("_"):
        continue

    if name.startswith("GLFW_"):
        macro_name = name[5:]
        _globals[macro_name] = getattr(GLFW, name)

    elif name.startswith("glfw"):
        function_name = re.sub('(?!^)([A-Z]+)', r'_\1',name[4:]).lower()
        _globals[function_name] = getattr(GLFW, name)

GLFW._error_reporting_query_func = lambda: ERROR_REPORTING
