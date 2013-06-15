import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires=[
    'SQLAlchemy',
    'pyramid',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_redis_sessions',
    'redis',
    'transaction',
    'zope.sqlalchemy',
]

setup(name='watchshop',
      version='0.1',
      description='watchshop',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Roman Sakal',
      author_email='sakalr@gmail.com',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="watchshop",
      entry_points = """\
      [paste.app_factory]
      main = watchshop:main
      """,
      paster_plugins=['pyramid'],
      )
