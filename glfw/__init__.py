"""
Python bindings for GLFW.
"""

__author__ = 'Florian Rhiem (florian.rhiem@gmail.com)'
__copyright__ = 'Copyright (c) 2013-2016 Florian Rhiem'
__license__ = 'MIT'
__version__ = '1.6'

# By default (ERROR_REPORTING = True), GLFW errors will be reported as Python
# exceptions. Set ERROR_REPORTING to False or set a curstom error callback to
# disable this behavior.
ERROR_REPORTING = True

# By default (NORMALIZE_GAMMA_RAMPS = True), gamma ramps are expected to
# contain values between 0 and 1, and the conversion to unsigned shorts will
# be performed internally. Set NORMALIZE_GAMMA_RAMPS to False if you want
# to disable this behavior and use integral values between 0 and 65535.
NORMALIZE_GAMMA_RAMPS = True

from . import GLFW
import re

_globals = globals()

for name in dir(GLFW):
    if name.startswith("GLFW_"):
        macro_name = name[5:]
        _globals[macro_name] = getattr(GLFW, name)

    elif name.startswith("glfw"):
        function_name = re.sub('(?!^)([A-Z]+)', r'_\1',name[4:]).lower()
        _globals[function_name] = getattr(GLFW, name)

GLFW._error_reporting_query_func = lambda: ERROR_REPORTING

GLFW._normalize_gamma_ramps_query_func = lambda: NORMALIZE_GAMMA_RAMPS