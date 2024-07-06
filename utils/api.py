import requests
from config.settings import API_BASE_URL

def get_robot_data(evm_address):
    response = requests.get(f'{API_BASE_URL}/robots/{evm_address}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to fetch robot data')

def get_trust_score(data):
    response = requests.post(f'{API_BASE_URL}/trust_score', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to get trust score')