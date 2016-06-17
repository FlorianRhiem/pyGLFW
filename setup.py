from distutils.core import setup
import os.path
import shutil
import subprocess

def create_required_files():
    '''
    Creates the files required for building a package.
    '''
    # Manifest
    if not os.path.isfile('MANIFEST.in'):
        with open('MANIFEST.in', 'w') as manifest_in:
            manifest_in.write('include *.txt')
    # License
    if not os.path.isfile('LICENSE.txt'):
        shutil.copyfile('LICENSE', 'LICENSE.txt')
    # Readme in reST format
    if not os.path.isfile('README.txt'):
        subprocess.call(['pandoc', 'README.md', '-t', 'rst', '-o', 'README.txt'])

create_required_files()
# README.txt was created in the function above, so we can use its content for
# the long description:
with open('README.txt') as file:
    long_description = file.read()

setup(name='glfw',
      version='1.2.0',
      description='A ctypes-based wrapper for GLFW3.',
      long_description=long_description,
      author='Florian Rhiem',
      author_email='florian.rhiem@gmail.com',
      url='https://github.com/FlorianRhiem/pyGLFW',
      classifiers = [
                    'Development Status :: 5 - Production/Stable',
                    'Environment :: MacOS X',
                    'Environment :: X11 Applications',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python',
                    'Topic :: Multimedia :: Graphics',
                    'Topic :: Scientific/Engineering :: Visualization',
                    ],
      py_modules=['glfw'],
      )
