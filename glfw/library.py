"""
Python bindings for GLFW.
"""

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import ctypes
import os
import glob
import sys
import subprocess
import textwrap


def _find_library_candidates(library_names,
                             library_file_extensions,
                             library_search_paths):
    """
    Finds and returns filenames which might be the library you are looking for.
    """
    candidates = set()
    for library_name in library_names:
        for search_path in library_search_paths:
            glob_query = os.path.join(search_path, '*'+library_name+'*')
            for filename in glob.iglob(glob_query):
                filename = os.path.realpath(filename)
                if filename in candidates:
                    continue
                basename = os.path.basename(filename)
                if basename.startswith('lib'+library_name):
                    basename_end = basename[len('lib'+library_name):]
                elif basename.startswith(library_name):
                    basename_end = basename[len(library_name):]
                else:
                    continue
                for file_extension in library_file_extensions:
                    if basename_end.startswith(file_extension):
                        if basename_end[len(file_extension):][:1] in ('', '.'):
                            candidates.add(filename)
                    if basename_end.endswith(file_extension):
                        basename_middle = basename_end[:-len(file_extension)]
                        if all(c in '0123456789.' for c in basename_middle):
                            candidates.add(filename)
    return candidates


def _load_library(library_names, library_file_extensions,
                  library_search_paths, version_check_callback):
    """
    Finds, loads and returns the most recent version of the library.
    """
    candidates = _find_library_candidates(library_names,
                                          library_file_extensions,
                                          library_search_paths)
    library_versions = []
    for filename in candidates:
        version = version_check_callback(filename)
        if version is not None and version >= (3, 0, 0):
            library_versions.append((version, filename))

    if not library_versions:
        return None
    library_versions.sort()
    return ctypes.CDLL(library_versions[-1][1])


def _glfw_get_version(filename):
    """
    Queries and returns the library version tuple or None by using a
    subprocess.
    """
    version_checker_source = '''
        import sys
        import ctypes

        def get_version(library_handle):
            """
            Queries and returns the library version tuple or None.
            """
            major_value = ctypes.c_int(0)
            major = ctypes.pointer(major_value)
            minor_value = ctypes.c_int(0)
            minor = ctypes.pointer(minor_value)
            rev_value = ctypes.c_int(0)
            rev = ctypes.pointer(rev_value)
            if hasattr(library_handle, 'glfwGetVersion'):
                library_handle.glfwGetVersion(major, minor, rev)
                version = (major_value.value,
                           minor_value.value,
                           rev_value.value)
                return version
            else:
                return None

        try:
            input_func = raw_input
        except NameError:
            input_func = input
        filename = input_func().strip()

        try:
            library_handle = ctypes.CDLL(filename)
        except OSError:
            pass
        else:
            version = get_version(library_handle)
            print(version)
    '''

    args = [sys.executable, '-c', textwrap.dedent(version_checker_source)]
    process = subprocess.Popen(args, universal_newlines=True,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = process.communicate(filename)[0]
    out = out.strip()
    if out:
        return eval(out)
    else:
        return None


def _get_library_search_paths():
    """
    Returns a list of library search paths, considering of the current working
    directory, default paths and paths from environment variables.
    """
    package_path = os.path.abspath(os.path.dirname(__file__))
    search_paths = [
        '',
        package_path,
        sys.prefix + '/lib',
        '/usr/lib64',
        '/usr/local/lib64',
        '/usr/lib', '/usr/local/lib',
        '/opt/homebrew/lib',
        '/run/current-system/sw/lib',
        '/usr/lib/x86_64-linux-gnu/',
        '/usr/lib/aarch64-linux-gnu/',
    ]

    if sys.platform != 'darwin':
        # manylinux2014 wheels contain libraries built for X11 and Wayland
        if os.environ.get('XDG_SESSION_TYPE') == 'wayland':
            search_paths.insert(1, os.path.join(package_path, 'wayland'))
        else:
            # X11 is the default, even if XDG_SESSION_TYPE is not set
            search_paths.insert(1, os.path.join(package_path, 'x11'))

    if sys.platform == 'darwin':
        path_environment_variable = 'DYLD_LIBRARY_PATH'
    else:
        path_environment_variable = 'LD_LIBRARY_PATH'
    if path_environment_variable in os.environ:
        search_paths.extend(os.environ[path_environment_variable].split(':'))
    return search_paths


if os.environ.get('PYGLFW_LIBRARY', ''):
    try:
        glfw = ctypes.CDLL(os.environ['PYGLFW_LIBRARY'])
    except OSError:
        glfw = None
elif sys.platform == 'win32':
    glfw = None  # Will become `not None` on success.

    # try Windows default search path
    try:
        glfw = ctypes.CDLL('glfw3.dll')
    except OSError:
        pass

    # try package directory
    if glfw is None:
        try:
            if sys.maxsize > 2**32:
                # load Microsoft Visual C++ 2012 runtime on 64-bit systems
                msvcr = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'msvcr110.dll'))
            else:
                # load Microsoft Visual C++ 2010 runtime on 32-bit systems
                msvcr = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'msvcr100.dll'))
            glfw = ctypes.CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'glfw3.dll'))
        except OSError:
            pass

    # try conda's default location on Windows
    if glfw is None:
        try:
            glfw = ctypes.CDLL(os.path.join(sys.prefix, 'Library', 'bin', 'glfw3.dll'))
        except OSError:
            pass
else:
    glfw = _load_library(['glfw', 'glfw3'], ['.so', '.dylib'],
                          _get_library_search_paths(), _glfw_get_version)
