import requests
from config.settings import API_BASE_URL, MBD_API_KEY

# def get_robot_data(evm_address):
#     try:
#         response = requests.get(f'{API_BASE_URL}/robots/{evm_address}')
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching robot data: {e}")
#         raise Exception('Failed to fetch robot data') from e

# def get_trust_score(data):
#     try:
#         response = requests.post(f'{API_BASE_URL}/trust_score', json=data)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error getting trust score: {e}")
#         raise Exception('Failed to get trust score') from e

def get_similar_users(user_id, top_k=10):
    url = "https://api.mbd.xyz/v1/farcaster/users/feed/similar"
    payload = {
        "user_id": user_id,
        "top_k": top_k
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": MBD_API_KEY
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json().get("body", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching similar users: {e}")
        raise Exception('Failed to fetch similar users') from e

def calculate_social_score(user_id):
    similar_users = get_similar_users(user_id)
    base_score = 80
    if len(similar_users) > 10:
        base_score += 5
    return base_score
