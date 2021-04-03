from setuptools import setup

# Original Code
# https://github.com/lcharleux/abapy.git

setup(name='abapy',
      version='0.1',
      description="Finite element pre/post processing using Python",
      long_description="",
      author='Ludovic Charleux, Vincent Keryvin',
      author_email='ludovic.charleux@univ-savoie.fr',
      license='GPL v2',
      packages=['abapy', 'abapy/spym'],
      zip_safe=False,
      install_requires=[
          "numpy",
          "scipy",
          "matplotlib"
          ],
      )
