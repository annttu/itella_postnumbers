from codecs import open
import pypandoc
from setuptools import setup, find_packages

description = "Thin wrapper for pandoc."
try:
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, OSError):
    print('check that you have installed pandoc properly and that README.md exists!')
    long_description = "A simple library to fetch and parse Itella's poorly formatted postnumber and postoffice data to python data structure."



setup(name='itella_postnumbers',
      version='0.1',
      description="fetch and parse itella postnumbers and postoffices",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Antti Jaakkola',
      author_email='annttu@itella_postnumbers.annttu.fi',
      url='https://github.com/annttu/itella_postnumbers',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      extras_require={
          'test': ['pytest']
      }
      )
