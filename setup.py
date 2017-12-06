"""
Publish a new version:

$ git tag X.Y.Z -m "Release X.Y.Z"
$ git push --tags

$ pip install --upgrade twine wheel
$ python setup.py sdist bdist_wheel --universal
$ twine upload dist/*
"""
from setuptools import setup

setup(
    name='damocles',
    packages=['damocles'],
    version='0.0.1',
    description='Job scheduling for humans.',
    license='MIT',
    author='Daniel Bader',
    author_email='mail@dbader.org',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
)
