import requests
from config.settings import API_BASE_URL, MBD_API_KEY

def get_robot_data(evm_address):
    response = requests.get(f'{API_BASE_URL}/robots/{evm_address}')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to fetch robot data')

def get_social_score(fid):
    nRes = get_most_recent_casts_for_user_from_fid(fid)
    ids = [cast['item_id'] for cast in nRes]
    mRes = get_emotion_labels(ids)

    count = 0
    total_trust = 0
    for current in mRes:
        if "trust" in current['labels']['emotion']:
            total_trust += current['labels']['emotion']['trust']
            count += 1

    social_score = total_trust * 100 / count if count > 0 else 0
    return social_score

def get_most_recent_casts_for_user_from_fid(fid):
    url = "https://api.mbd.xyz/v1/farcaster/casts/feed/for-you"
    payload = {
        "user_id": fid,
        "top_k": 50,
        "return_ai_labels": True
    }
    headers = {
        "accept": "application/json",
        "HTTP-Referer": "https://docs.mbd.xyz/",
        "X-Title": "mbd_docs",
        "content-type": "application/json",
        "x-api-key": MBD_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception('Failed to fetch casts for user with fid: ', fid)

    return response.json().get("body", [])

def get_emotion_labels(ids):
    url = "https://api.mbd.xyz/v1/farcaster/casts/labels/for-items"
    payload = {
        "items_list": ids,
        "label_category": "emotion"
    }
    headers = {
        "accept": "application/json",
        "HTTP-Referer": "https://docs.mbd.xyz/",
        "X-Title": "mbd_docs",
        "content-type": "application/json",
        "x-api-key": MBD_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception('Failed to fetch emotion labels')

    return response.json().get("body", [])

if __name__ == "__main__":
    vitalik_user_id = '12345'  # Replace with actual user ID
    social_score = get_social_score(vitalik_user_id)
    print(f"Social score of user {vitalik_user_id} is {social_score}")
