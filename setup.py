#!/usr/bin/env python

from pathlib import Path
import configparser
import re

from setuptools import setup


MODULE_DIR = Path(__file__).resolve().parent


def read(fname):
    return (MODULE_DIR / fname).read_text(encoding='utf-8')


config = configparser.ConfigParser()
with (MODULE_DIR / 'tryton.cfg').open(encoding='utf-8') as cfg_file:
    config.read_file(cfg_file)
info = dict(config.items('tryton'))

for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
major_version, minor_version = 6, 0

requires = []

fiuner_modules = [
    'health_appointment_fiuner',
    'health_appointment_screen_fiuner',
]

for dep in info.get('depends', []):
    if dep in fiuner_modules:
        requires.append('%s == %s' % (dep, info.get('version')))
    elif dep == 'health':
        requires.append('gnuhealth == %s' % (info.get('version')))
    elif dep.startswith('health_') and dep not in fiuner_modules:
        health_package = dep.split('_', 1)[1]
        requires.append('gnuhealth_%s == %s' %
            (health_package, info.get('version')))
    else:
        if not re.match(r'(ir|res|webdav)(\W|$)', dep):
            requires.append('trytond_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))

requires.append('trytond >= %s.%s, < %s.%s' %
    (major_version, minor_version, major_version, minor_version + 1))

setup(
    name='z_health_consulting_rooms',
    version=info.get('version', '0.0.1'),
    description=info.get(
        'description',
        'GNU Health HMIS: modulo FIUNER para consultorios'),
    long_description=read('README.rst'),
    author='',
    author_email='',
    url='',
    download_url='',
    package_dir={'trytond.modules.z_health_consulting_rooms': '.'},
    packages=[
        'trytond.modules.z_health_consulting_rooms',
    ],
    package_data={
        'trytond.modules.z_health_consulting_rooms': info.get('xml', []) +
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
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    license='GPL-3',
    python_requires='>=3.10,<3.11',
    install_requires=requires,
    extras_require={},
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    z_health_consulting_rooms = trytond.modules.z_health_consulting_rooms
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
