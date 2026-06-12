from setuptools import setup, find_packages

setup(
  name="mikrohelpers",
  version="0.5",
  packages=find_packages(),
  install_requires=[
    "flet",
    "bcrypt",
    "python-dotenv",
    "cryptography"
  ],
  description="Package helpers to Mikro Monitor apk",
  url="https://github.com/mikroangkot/assets",
  author="RumahDjigo",
  author_email="rumahdjigo@gmail.com",
  license="MIT"
)
