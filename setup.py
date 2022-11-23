#!/usr/bin/env python

from setuptools import setup
from os import path
import os
with open("requirements.txt",'r') as f:
    requirements = f.readlines()

setup(
  name = 'DiffVAE',         # How you named your package folder (MyLib)
  packages = ['DiffVAE'],   # Chose the same as "name"
  version = '0.100',      # Start with a small number and increase it with every change you make
  license='X',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library that achieves DiffuseVAE for TTS',   # Give a short description about your library
  #long_description=read_file('README.md'),
  long_description='https://github.com/ZJLEOWANG3/X',
  long_description_content_type='text/markdown',  
  author = 'Zijian Leo Wang',                   # Type in your name
  author_email = 'zjleowang3@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ZJLEOWANG3/X.git',   # Provide either the link to your github or to your website
  keywords = ['DL', 'TTS', 'Generative Model'],   # Keywords that define your package best
  include_package_data=False,
  install_requires=requirements,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: X License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',
  ],
)
