
from setuptools import setup

setup(
    name='django_thecodebase',
    packages=['django_thecodebase'],
    include_package_data=True,
    install_requires=[
        'django',
        'psycopg2',
        'passlib',
        'markdown',
        'icalendar',
        'PyGithub',
        'requests',
    ],
)
