from setuptools import setup, find_packages

setup(name='pywhale',
      version='0.1',
      description='Whaleclub.co cryptocurrency Exchange API Pyhon Client',
      url='http://github.com/xmatthias/pywhale',
      author='Logan Schwartz, Matthias Voppichler',
      author_email='xmatthias@outlook.com',
      license='GPL3',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
      zip_safe=False)
