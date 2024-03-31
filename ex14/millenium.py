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


pilot_url = "https://swapi.dev/api/people/13/"
base_url = 'https://swapi.dev/api/starships/?search=Millennium Falcon'
ship_data = get_infoship(base_url)['results'][0]
pilot_data = get_infopilots(pilot_url)


infopilots = {
    "name": pilot_data['name'],
    "height": pilot_data['height'],
    "weight": pilot_data['mass'],
    "homeworld":
        {'name': get_name_homeworld(pilot_data['homeworld']),
        'link': pilot_data['homeworld']}

    }

infoship = {
    'name': ship_data['name'],
    'max_speed': ship_data['max_atmosphering_speed'],
    'class': ship_data['starship_class'],
    'pilots': [infopilots]

}
for pilot_url in ship_data['pilots']:

print(infoship)


# response = requests.get(url=base_url)
# data = response.json()

# # https://swapi.dev/api/starships/?search=Millennium
# # ship_data = response.json()['results'][1]['name']
# ship_data['name'] = response.json()['results'][0]['name']
# ship_data['max_atmosphering_speed'] = response.json()['results'][0]['max_atmosphering_speed']
# ship_data['starship_class'] = response.json()['results'][0]['starship_class']
# # ship_data['pilots'] = []
#

# for PILOT_URL in response.json() :
#     print(PILOT_URL)
#     response = requests.get(url=PILOT_URL)
#     ship_data['pilots'] = [response.json()['name']]
#     # print(response.json())
#     # ship_data['pilots'] =
# # ship_data2 = response.json()
# # print(response.json()['results']['name'])
#
# # print(ship_data2['results'])
# print(ship_data)
#
# # with open('ship_data.json', 'w') as write_file:
# #     json.dump(ship_data, write_file, indent=2)
