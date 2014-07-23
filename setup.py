import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="django-upload",
    version="0.1",
    license="MIT",
    description="Django upload - upload multiple files and get a gallery",
    long_description=readme,
    install_requires=['Django>=1.3'],
    url="https://github.com/savioabuga/django-upload",
    author="Savio Abuga",
    author_email="savioabuga@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
       "Development Status :: 5 - Production/Stable",
       "Operating System :: OS Independent",
       "License :: OSI Approved :: MIT License",
       "Intended Audience :: Developers",
       "Programming Language :: Python :: 2.6",
       "Programming Language :: Python :: 2.7"
    ]
)
