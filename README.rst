pyGLFW
======

This module provides Python bindings for `GLFW <http://www.glfw.org/>`__
(on GitHub: `glfw/glfw <http://github.com/glfw/glfw>`__). It is a
``ctypes`` wrapper which keeps very close to the original GLFW API,
except for:

-  function names use the pythonic ``words_with_underscores`` notation
   instead of ``camelCase``
-  ``GLFW_`` and ``glfw`` prefixes have been removed, as their function
   is replaced by the module namespace
   (you can use ``from glfw.GLFW import *`` if you prefer the naming
   convention used by the GLFW C API)
-  structs have been replaced with Python sequences and namedtuples
-  functions like ``glfwGetMonitors`` return a list instead of a pointer
   and an object count
-  Gamma ramps use floats between 0.0 and 1.0 instead of unsigned shorts
   (use ``glfw.NORMALIZE_GAMMA_RAMPS=False`` to disable this)
-  GLFW errors are reported as ``glfw.GLFWError`` warnings if no error
   callback is set (use ``glfw.ERROR_REPORTING=False`` to disable this,
   set it to 'warn' instead to issue warnings, set it to 'log' to log it
   using the 'glfw' logger or set it to a dict to define the behavior for
   specific error codes)
-  instead of a sequence for ``GLFWimage`` structs, PIL/pillow ``Image``
   objects can be used

Installation
------------

pyGLFW can be installed using pip:

.. code:: sh

    pip install glfw

Windows
~~~~~~~

The GLFW shared library and Visual C++ runtime are included in the Python wheels.

To use a different GLFW library, you can set ``PYGLFW_LIBRARY`` to its location.

macOS
~~~~~

The GLFW shared library for 64-bit is included in the Python wheels for macOS.

If you are using a 32-bit Python installation or otherwise cannot use the
library downloaded with the wheel, you can build and install it yourself by
`compiling GLFW from source <http://www.glfw.org/docs/latest/compile.html>`__
(use ``-DBUILD_SHARED_LIBS=ON``).

pyGLFW will search for the library in a list of search paths (including those
in ``DYLD_LIBRARY_PATH``). If you want to use a specific library, you can set
the ``PYGLFW_LIBRARY`` environment variable to its path.

Linux
~~~~~

The GLFW shared library is included in the Python wheels for Linux. Although
pyGLFW will try to detect whether the GLFW library for Wayland or X11 should
be used, you can set the ``PYGLFW_LIBRARY_VARIANT`` variable to ``wayland`` or
``x11`` to select either variant of the library.

If you cannot use these on your system, you can install the GLFW shared
library using a package management system (e.g. ``apt install libglfw3``
on Debian or Ubuntu) or you can build and install it yourself by
`compiling GLFW from source <http://www.glfw.org/docs/latest/compile.html>`__
(use ``-DBUILD_SHARED_LIBS=ON``).

pyGLFW will search for the library in a list of search paths (including those
in ``LD_LIBRARY_PATH``). If you want to use a specific library, you can set
the ``PYGLFW_LIBRARY`` environment variable to its path.

Development Version
~~~~~~~~~~~~~~~~~~~

If you are using the development version of GLFW and would like to use wrappers
for currently unreleased macros and functions, you can instead install:

.. code:: sh

    pip install glfw[preview]

or set the ``PYGLFW_PREVIEW`` environment variable.

Note, however, that there will be a slight delay between the development
version of GLFW and the wrappers provided by this package.

Example Code
------------

The example from the `GLFW
documentation <http://www.glfw.org/documentation.html>`__ ported to
pyGLFW:

.. code:: python

    import glfw

    def main():
        # Initialize the library
        if not glfw.init():
            return
        # Create a windowed mode window and its OpenGL context
        window = glfw.create_window(640, 480, "Hello World", None, None)
        if not window:
            glfw.terminate()
            return

        # Make the window's context current
        glfw.make_context_current(window)

        # Loop until the user closes the window
        while not glfw.window_should_close(window):
            # Render here, e.g. using pyOpenGL

            # Swap front and back buffers
            glfw.swap_buffers(window)

            # Poll for and process events
            glfw.poll_events()

        glfw.terminate()

    if __name__ == "__main__":
        main()
