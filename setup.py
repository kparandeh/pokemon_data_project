from setuptools import setup, find_packages

setup(
    name='pokemon_data',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Kyan Parandeh',
    author_email='kparandeh@protonmail.com',
    description='A Python package to fetch Pokémon evolution data using PokeAPI.',
    keywords='pokemon evolution api'
)