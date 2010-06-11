# -*- encoding: utf-8 -*-
from setuptools import setup

setup(
    name='django-seltest',
    version='0.1',
    description="Selenium test integration for Django based projects.",
    long_description=open('README').read(),
    author='Fabián Ezequiel Gallina',
    author_email='fabian@gnu.org.ar',
    url='http://github.com/fgallina/seltest',
    packages=['seltest'],
    package_dir={'seltest': 'seltest'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: GNU/Linux',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
