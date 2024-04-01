import requests
import json


def get_infoship(url):
    response = requests.get(url)
    data = response.json()
    return data


def get_infopilots(pilot_url):
    response = requests.get(pilot_url)
    pilot_data = response.json()
    return pilot_data


def get_name_homeworld(link_homeworld):
    homeworld_response = requests.get(link_homeworld)
    homeworld_data = homeworld_response.json()
    return homeworld_data['name']


def main():
    base_url = 'https://swapi.dev/api/starships/'
    ships_data = get_infoship(base_url)['results']

    for ship in ships_data:
        if ship['name'] == 'Millennium Falcon':
            ship_data = get_infoship(ship['url'])
            break
    infopilots = []
    for pilot_url in ship_data['pilots']:
        pilot_data = get_infopilots(pilot_url)
        infopilot = {
            'name': pilot_data['name'],
            'height': pilot_data['height'],
            'weight': pilot_data['mass'],
            'homeworld':
            {'name': get_name_homeworld(pilot_data['homeworld']), 'link': pilot_data['homeworld']}
        }
        infopilots.append(infopilot)

    infoship = {
        'name': ship_data['name'],
        'max_speed': ship_data['max_atmosphering_speed'],
        'class': ship_data['starship_class'],
        'pilots': infopilots}


    print(infoship)


    with open('ship_data.json', 'w') as write_file:
        json.dump(infoship, write_file, indent=2)

if __name__ == "__main__":
    main()
