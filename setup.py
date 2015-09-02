from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n')

setup(name='medialog.fullpagebehavior',
      version=version,
      description="A behavior to add richtect tuple field and a fullpage view",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='behavior rich text fields medialog plone',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.fullpagebehavior',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.dexterity',
          'collective.z3cform.datagridfield',
          'plone.directives.form',
          'plone.behavior',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
