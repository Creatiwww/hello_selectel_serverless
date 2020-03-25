import requests
import json

def get_cases():
    url = 'https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php'

    headers = {
        'x-rapidapi-host': 'coronavirus-monitor.p.rapidapi.com',
        'x-rapidapi-key': 'f9dd3a4723msh657a023a6e89098p16e0fbjsndb7b9ab21c26'
        }

    response = requests.request("GET", url, headers=headers)
    out = json.loads(response.text)

    return out
