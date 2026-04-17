#!/usr/bin/env python

from setuptools import setup
import re
import os
import configparser


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


config = configparser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))

for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version = 6, 0

requires = []

fiuner_modules = ['health_appointment_screen_fiuner']

for dep in info.get('depends', []):
    if dep == 'health':
        requires.append('gnuhealth == %s' % (info.get('version')))
    elif dep.startswith('health_') and dep not in fiuner_modules:
        health_package = dep.split('_', 1)[1]
        requires.append('gnuhealth_%s == %s' %
            (health_package, info.get('version')))
    else:
        if not re.match(r'(ir|res|webdav)(\W|$)', dep) and dep not in fiuner_modules:
            requires.append('trytond_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))

requires.append('trytond >= %s.%s, < %s.%s' %
    (major_version, minor_version, major_version, minor_version + 1))

setup(
    name='health_consultorios_fiuner',
    version=info.get('version', '0.0.1'),
    description=info.get(
        'description',
        'GNU Health HMIS: modulo FIUNER para consultorios'),
    long_description=read('README.rst'),
    author='',
    author_email='',
    url='',
    download_url='',
    package_dir={'trytond.modules.health_consultorios_fiuner': '.'},
    packages=[
        'trytond.modules.health_consultorios_fiuner',
    ],
    package_data={
        'trytond.modules.health_consultorios_fiuner': info.get('xml', []) +
        info.get('translation', []) +
        ['tryton.cfg', 'view/*.xml'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    license='GPL-3',
    install_requires=requires,
    extras_require={},
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    health_consultorios_fiuner = trytond.modules.health_consultorios_fiuner
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
