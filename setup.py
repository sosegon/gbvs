from setuptools import setup, find_packages

setup(name='gbvs',
      version='0.1',
      description='A package for calculating gbvs',
      packages=find_packages(),
      data_files=[('', ['28__32__m__2.mat'])],
      zip_safe=False)