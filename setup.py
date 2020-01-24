from setuptools import setup

setup(
    name='Unix Tree Copy',
    version= '1.0',
    py_modules = ['unix'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        unix=unix:cli
    ''',
) 