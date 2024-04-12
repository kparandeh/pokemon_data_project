# Pokemon Data

This Python package allows users to fetch the evolution paths of Pokémon using the Pokémon API (PokeAPI).

## Installation

Clone this repository:
- Open your command line and enter:
git clone https://github.com/kparandeh/pokemon_data_project.git

Navigate to the project directory:

cd pokemon_data_project

Install the package:
python setup.py install

To install the required dependencies, run:
pip install -r requirements.txt

## Usage

Import the package and use it as follows:

```python
from analysis.evolutions import get_pokemon_evolution

evolution_path = get_pokemon_evolution("bulbasaur")
print(evolution_path)