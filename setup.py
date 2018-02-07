from setuptools import setup, find_packages

setup(
    name='WallE',
    version='1.0.5',
    description='A ROS wrapper',
    url='https://github.com/tianhaoz95/WallE',
    author='Jason Tyanhau Chiau',
    author_email='tyan_chiau@berkeley.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Robotics',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['test'])
)
