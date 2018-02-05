from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='WallE',
    version='1.0.1',
    description='A ROS wrapper',
    url='https://github.com/pypa/sampleproject',
    author='Jason Tyanhau Chiau',
    author_email='tyan_chiau@berkeley.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Robotics',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='robotics',
    packages=find_packages()
)
