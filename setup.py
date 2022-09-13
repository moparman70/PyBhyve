'''
    PyBhyve
    ------------

    Communication tool for the B-Hyve water timer device.


'''
import re
import sys
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='PyBhyve',
    version='0.0.2',
    url='https://github.com/moparman70/PyBhyve',
    license='GNU GPL v3',
    description='Communication tool for the B-Hyve water timer devices',
    author='',
    author_email='',
    maintainer='',
    maintainer_email='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pybhyvee = pybhyvee.__init__:main'
        ],
    },
)
