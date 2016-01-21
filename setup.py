from distutils.core import setup
import os

import codecs

with codecs.open("readme.rst", encoding="utf-8") as f:
    DESCRIPTION = f.read()

setup(
    name='django-mailhide',
    version='1.0.2',
    packages=['django_mailhide', 'django_mailhide.templatetags'],
    url='https://github.com/jbzdak/django-mailhide',
    license='BSD-style two clause',
    author='Jacek Bzdak',
    author_email='jbzdak@gmail.com',
    description=DESCRIPTION,
    install_requires=[
        'pycrypto>=2.6.1,<3.0.0',
    ],
    package_data={'django_mailhide': ['templates/mailhide/*.html']},
    classifiers="""
Development Status :: 5 - Production/Stable
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: Polish
Natural Language :: English
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
    """
)
