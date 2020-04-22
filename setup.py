from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'xpx', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='xpx',
    version=version['__version__'],
    description=('XPSWMM .xpx format file libarry.'),
    long_description=long_description,
    author='Mel Meng',
    author_email='melmeng@hotmail.com',
    url='https://github.com/mel-meng/xpx',
    license='MPL-2.0',
    packages=['xpx'],
#   no dependencies in this example
#   install_requires=[
#       'dependency==1.2.3',
#   ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    )
