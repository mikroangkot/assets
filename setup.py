from setuptools import setup, find_packages

setup(
  name="mikrohelpers",
  version="1.0.8",
  description="Package helpers to format intern data",
  url="https://github.com/mikroangkot/assets",
  author="RumahDjigo",
  author_email="rumahdjigo@gmail.com",
  license="MIT",
  package_dir={"": "src"},
  packages=find_packages(where="src"),
  install_requires=[
    "flet",
    "bcrypt",
    "python-dotenv",
    "cryptography"
  ]
)
