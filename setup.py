__author__ = 'Filip'
from setuptools import setup

setup(
    name='PycklePi',
    version='1.1',
    description="PycklePi is a small module for controlling buttons, LED's and more on the Raspberry Pi",
    url='https://github.com/filipherle/PycklePi',
    author='Filip',
    author_email='toxicnull@gmail.com',
    install_requires=[
        "RPi.GPIO >= 0.6.3"
    ],
    classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: Linux and OSX',
          'Programming Language :: Python',
    ]
)
