from setuptools import setup, find_namespace_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='phisuite.data',  # Required
    version='0.0.2',  # Required
    description='Phi Suite Data',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    url='https://github.com/phisuite/data.py',  # Optional
    author='Phi Skills',  # Optional
    author_email='phisuite@phiskills.com',  # Optional
    license='GNU GPLv3',  # Optional
    classifiers=[  # Optional
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    keywords='Phi Suite Data Engineering',  # Optional
    packages=find_namespace_packages(include=['phisuite.*']),  # Required
    python_requires='>=3.8, <4',
    install_requires=['protobuf', 'grpcio'],  # Optional
    project_urls={  # Optional
        'Project website': 'https://phisuite.com',
        'Company website': 'https://phiskills.com',
        'Documentation': 'https://phisuite.com/doc',
        'Source': 'https://github.com/phisuite/data.py',
    },
)
