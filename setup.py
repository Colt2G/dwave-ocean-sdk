# Copyright 2018 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

from setuptools import setup

# add __version__, __author__, __authoremail__, __description__ to this namespace
# equivalent to:
exec(open("./dwaveoceansdk/package_info.py").read())


install_requires = [
    'dimod==0.9.15',
    'dwave-cloud-client==0.8.6',
    'dwave-greedy==0.2.0',
    'dwave-hybrid==0.6.2',
    'dwave-inspector==0.2.6',
    'dwave-neal==0.5.7',
    'dwave-networkx==0.8.8',
    'dwave-preprocessing==0.2.0',
    'dwave-qbsolv==0.3.2',
    'dwave-system==1.6.0',
    'dwave-tabu==0.4.1',
    'dwavebinarycsp==0.1.2',
    'minorminer==0.2.6',
    'penaltymodel-cache==0.4.3',
    'penaltymodel-lp==0.1.4',
    'penaltymodel==0.16.4',
    'pyqubo==1.0.12'
]

# note: when updating the version of maxgap, it also must be updated in
# docs/requirements.txt.
extras_require = {
    ':(platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "AMD64")': [
        'penaltymodel-mip==0.2.4'
    ],
    ':platform_machine != "x86_64" and platform_machine != "amd64" and platform_machine != "AMD64"': [
        'penaltymodel-maxgap==0.5.4'  # see note above
    ],
    'all': ['penaltymodel-mip==0.2.4', 'penaltymodel-maxgap==0.5.4']
}


packages = ['dwaveoceansdk']

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

python_requires = '>=3.6'

setup(
    name='dwave-ocean-sdk',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave-ocean-sdk',
    long_description=open('README.rst').read(),
    classifiers=classifiers,
    python_requires=python_requires,
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require
)
