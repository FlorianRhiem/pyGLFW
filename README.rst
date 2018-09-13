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
-  GLFW errors are reported as ``glfw.GLFWError`` exceptions if no error
   callback is set (use ``glfw.ERROR_REPORTING=False`` to disable this)
-  instead of a sequence for ``GLFWimage`` structs, PIL/pillow ``Image``
   objects can be used

Installation
------------

pyGLFW can be installed using pip:

.. code:: sh

    pip install glfw

Windows
~~~~~~~

The GLFW shared library is included in the Python wheels for Windows, but the correct Microsoft Visual C++ Redistributable will be required:

- `VC 2010 <https://www.microsoft.com/en-us/download/details.aspx?id=5555>`_ for 32-bit Python, or
- `VC 2012 <https://www.microsoft.com/en-us/download/details.aspx?id=30679>`_ for 64-bit Python.

Alternatively, you can download a shared library built for a runtime already installed on your system from `glfw.org <http://www.glfw.org/download.html>`_.

Linux and macOS
~~~~~~~~~~~~~~~

You will need to install the GLFW shared library yourself and should
`compile GLFW from source <http://www.glfw.org/docs/latest/compile.html>`__
(use ``-DBUILD_SHARED_LIBS=ON``).

pyGLFW will search for the library in a list of search paths (including those
in ``LD_LIBRARY_PATH`` on Linux and ``DYLD_LIBRARY_PATH`` on macOS). If you
want to use a specific library, you can set the ``PYGLFW_LIBRARY`` environment
variable to its path.

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
