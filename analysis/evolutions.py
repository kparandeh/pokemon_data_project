import requests

def get_pokemon_evolution(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}/"
    response = requests.get(url)
    species_data = response.json()

    evolution_chain_url = species_data['evolution_chain']['url']
    response = requests.get(evolution_chain_url)
    evolution_data = response.json()

    def extract_evolutions(evo_chain):
        """
        Recursively extract the evolution paths.
        """
        current_stage = evo_chain['species']['name']
        if not evo_chain['evolves_to']:
            return [[current_stage]]
        
        evolutions = []
        for evolution in evo_chain['evolves_to']:
            for path in extract_evolutions(evolution):
                evolutions.append([current_stage] + path)
        return evolutions

    return extract_evolutions(evolution_data['chain'])

# Example
evolution_path = get_pokemon_evolution("eevee")
for path in evolution_path:
    print(path)
