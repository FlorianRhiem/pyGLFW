pyGLFW
======

This module provides Python bindings for [GLFW](http://www.glfw.org/) (on GitHub: [glfw/glfw](http://github.com/glfw/glfw)). It is a `ctypes` wrapper which keeps very close to the original GLFW API, except for:

 - `GLFW_` and `glfw` prefixes have been removed, as their function is replaced by the module namespace
 - structs have been replaced with Python sequences
 - functions like `glfwGetMonitors` return a list instead of a pointer and an object count
 - Gamma ramps use floats between 0.0 and 1.0 instead of unsigned shorts

Example Code
------------
The example from the [GLFW documentation](http://www.glfw.org/documentation.html) ported to pyGLFW:

```python
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
```
