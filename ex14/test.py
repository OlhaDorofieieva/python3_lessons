import requests
import json

def get_ship_info(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_pilot_info(pilot_url):
    response = requests.get(pilot_url)
    pilot_data = response.json()
    homeworld_response = requests.get(pilot_data['homeworld'])
    homeworld_data = homeworld_response.json()
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'weight': pilot_data['mass'],
        'homeworld': {
            'name': homeworld_data['name'],
            'link': pilot_data['homeworld']
        }
    }
    return pilot_info

def main():
    ship_url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
    ship_data = get_ship_info(ship_url)['results'][0]

    ship_info = {
        'name': ship_data['name'],
        'max_speed': ship_data['max_atmosphering_speed'],
        'class': ship_data['starship_class'],
        'pilots': []
    }

    for pilot_url in ship_data['pilots']:
        pilot_info = get_pilot_info(pilot_url)
        ship_info['pilots'].append(pilot_info)

    with open('millennium_falcon.json', 'w') as file:
        json.dump(ship_info, file, indent=4)

if __name__ == "__main__":
    main()