from setuptools import setup, find_packages

setup(
  name="mikrohelpers",
  version="0.6",
  description="Package helpers to format intern data",
  url="https://github.com/mikroangkot/assets",
  author="RumahDjigo",
  author_email="rumahdjigo@gmail.com",
  license="MIT"
  packages=find_packages(where="src"),
  packages_dir={"": "src"},
  install_requires=[
    "flet",
    "bcrypt",
    "python-dotenv",
    "cryptography"
  ]
)
