from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='primer-py-money',
    packages=[
        'money'
    ],
    version='0.6.0',
    description='Money module for python with Primer specific subunits',
    long_description=long_description,
    url='https://github.com/primer-io/py-money',
    author='Primer',
    author_email='"developers@primer.io',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='money currency',
    install_requires=[
        'babel >= 2.4.0, < 3.0'
    ],
)
