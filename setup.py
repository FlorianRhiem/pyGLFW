from setuptools import setup
import os.path

setup_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_directory, 'README.rst')) as readme_file:
    long_description = readme_file.read()

setup(
    name='glfw',
    version='1.8.2',
    description='A ctypes-based wrapper for GLFW3.',
    long_description=long_description,
    url='https://github.com/FlorianRhiem/pyGLFW',
    author='Florian Rhiem',
    author_email='florian.rhiem@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    packages=['glfw'],
    package_data={
        # include GLFW shared library in wheel package
        'glfw': ['glfw3.dll']
    }
)
