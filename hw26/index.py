import requests
import json

# 1. Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc. 

def save_robots_file(website_path, file_name):
    with open(file_name, 'w') as file:
        response = requests.get(f'{website_path}/robots.txt')
        file.write(response.text)

save_robots_file('https://en.wikipedia.org', 'wikipedia_robots.txt')
save_robots_file('https://stackoverflow.com', 'stackoverflow_robots.txt')


# 2. Ознайомтесь з фрішним АПІ https://russianwarship.rip/api-documentation/v2. 
# (заг.сайт - https://russianwarship.rip/). Спробуйте попрацювати з 2-3 ендпоінтами (URL) 
# на вибір і завантажити отримані дані в JSON-файл 

war_status_response = requests.get('https://russianwarship.rip/api/v2/war-info/status/ua')
latest_statistic_response = requests.get('https://russianwarship.rip/api/v2/statistics/latest')
december_statistic_response = requests.get('https://russianwarship.rip/api/v2/statistics?date_from=2023-12-01&date_to=2023-12-31')


with open('war_info.json', 'w') as file:
    war_status_data = war_status_response.json()['data']
    latest_statistic_data = latest_statistic_response.json()['data']
    december_statistic_data = december_statistic_response.json()['data']

    war_data = {
        'status':  war_status_data,
        'statistics': {
            'latest': latest_statistic_data,
            'december': december_statistic_data
        }
    }

    file.write(json.dumps(war_data, indent=4))

