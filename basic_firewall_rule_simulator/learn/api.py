
import requests

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_info(name):
    url = f'{base_url}pokemon/{name}'
    respone = requests.get(url)

    if respone.status_code == 200:
        print('Success!')
        info_pokemon = respone.json()
        return info_pokemon
    else:
        print('Fail!')

pokemon_name = 'pikachu'
pokemon_info = get_pokemon_info(pokemon_name)
print(pokemon_info['name'], pokemon_info['height'])