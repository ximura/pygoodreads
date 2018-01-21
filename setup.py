from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='pygoodreads',
      version='1.0',
      description='Python wrapper for Goodreads API',
      author='ximura',
      author_email='',
      url='',
      packages=find_packages(exclude=['test', 'test.*']),
      python_requires='>=3.6',
      install_requires=install_requires
      )
