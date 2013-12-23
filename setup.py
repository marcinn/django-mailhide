from distutils.core import setup

import codecs

with codecs.open("readme.rst", encoding="utf-8") as f:
    DESCRIPTION = f.read()

setup(
    name='django-mailhide',
    version='1.0',
    packages=['django_mailhide', 'django_mailhide.templatetags'],
    url='https://pypi.python.org/pypi/django-mailhide',
    license='BSD-style two clause',
    author='Jacek Bzdak',
    author_email='jbzdak@gmail.com',
    description=DESCRIPTION
)
