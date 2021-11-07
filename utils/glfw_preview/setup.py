from setuptools import setup

setup(
    name='glfw_preview',
    version='0.0.3',
    description='A helper package for the glfw package.',
    long_description='This is a helper package for the glfw package that enables wrappers for unreleased GLFW3 macros and functions.',
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
    packages=['glfw_preview'],
)
