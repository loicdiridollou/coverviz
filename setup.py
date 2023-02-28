from setuptools import setup, find_packages


setup(
    name='coverviz',
    version='0.0.1',
    packages=find_packages(include=['coverviz', 'coverviz.*']),
    install_requires=['squarify', 'matplotlib', 'seaborn'],
)
