from setuptools import setup

setup(name='gaia_astero',
      version='0.1',
      description='Catalogues of Gaia stars with asteroseismic parameters',
      url='http://github.com/RuthAngus/gaia_astero',
      author='Ruth Angus',
      author_email='ruthangus@gmail.com',
      license='MIT',
      packages=['gaia_astero'],
      install_requires=['numpy', 'pandas'],
      include_package_data=True,
      zip_safe=False)
