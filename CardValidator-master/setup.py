import os
from setuptools import setup


short_description = 'Module to validate, generate and determine the format of card numbers.'

setup(
    name='Card Validator',
    version='1.0.0',
    author='Chetan Chadha',
    author_email='chetanchadha92@gmail.com',
    description=short_description,
    license='MIT',
    keywords='credit debit card generate validate numbers',
    url='',
    packages=['cardvalidator', 'tests'],
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
