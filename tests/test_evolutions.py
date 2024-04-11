from pokemon_data.analysis.evolutions import get_pokemon_evolution
import pytest

def test_get_pokemon_evolution_valid():
    """Test getting evolution path for a valid Pokémon name."""
    evolution_paths = get_pokemon_evolution('charmander')
    flattened_paths = [pokemon for path in evolution_paths for pokemon in path]
    assert 'charmeleon' in [pokemon.lower() for pokemon in flattened_paths]
