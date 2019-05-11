"""
This file imports glfw and converts constant and function names to the style
of the GLFW C API, adding GLFW_ and glfw prefixes and using CamelCase for
function names.

This file is only needed to be run when adding functions to the wrapper.
"""

from collections import OrderedDict
import glfw

constant_names = OrderedDict()
function_names = OrderedDict()
constant_type = int
function_type = type(glfw.init)
for pythonic_name in sorted(dir(glfw)):
    if pythonic_name.startswith('_'):
        continue
    obj = getattr(glfw, pythonic_name)
    if isinstance(obj, function_type):
        if pythonic_name == 'get_joystick_guid':
            cstyle_name = 'glfwGetJoystickGUID'
        else:
            cstyle_name = 'glfw' + ''.join(word.title() for word in pythonic_name.split('_'))
        function_names[pythonic_name] = cstyle_name
    elif isinstance(obj, constant_type):
        cstyle_name = 'GLFW_' + pythonic_name
        constant_names[pythonic_name] = cstyle_name
print('""" Automatically generated C-style module for pyGLFW """')
print('from . import (')
for pythonic_name, cstyle_name in constant_names.items():
    print('    {} as {},'.format(pythonic_name, cstyle_name))
for pythonic_name, cstyle_name in function_names.items():
    print('    {} as {},'.format(pythonic_name, cstyle_name))
print(')')
