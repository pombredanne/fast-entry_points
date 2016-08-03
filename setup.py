from setuptools import setup
import fastentrypoints

setup(
    name='fastentrypoints',
    version='0.1',
    py_modules=['fastentrypoints'],
    long_description=open('README.rst').read(),
    url='https://github.com/ninjaaron/fastentrypoints',
    author='Aaron Christianson',
    author_email='ninjaaron@gmail.com',
    license='BSD',
    entry_points={'console_scripts': ['fastep=fastentrypoints:main']},
)