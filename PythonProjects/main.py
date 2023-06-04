import requests
from faker import Faker

fake = Faker("ru_RU")
host = 'https://pokemonbattle.me:9104'
token = '5a12966ec0a93f326ea4bf5c9fad5a71'

сreation = requests.post(f'{host}/pokemons', json = 
                       {
    "name": fake.name(),
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(сreation.text)

сhange = requests.put(f'{host}/pokemons', json =
                      {
    "pokemon_id": "12866",
    "name": fake.name(),
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(сhange.text)

catch = requests.post(f'{host}/trainers/add_pokeball', json =
                      {
    "pokemon_id": "12866"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(catch.text)