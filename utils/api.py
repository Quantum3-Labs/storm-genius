import requests
import openai
from config.settings import API_BASE_URL, MBD_API_KEY, ETH_NODE_URL, CONTRACT_ADDRESS, CONTRACT_ABI, PRIVATE_KEY
from web3 import Web3

# Connect to the network
web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

# Verify if the connection is successful
if web3.is_connected():
    print("-" * 50)
    print("Connection Successful")
    print("-" * 50)
else:
    print("Connection Failed")

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
        "filters": { "ai_labels": ["trust"] },
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
        raise Exception(f'Failed to fetch casts for user with fid: {fid}')

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

def get_gpt_explanation(social_score):
    # openai.api_key = OPENAI_API_KEY
    # prompt = f"The social score of the user is {social_score}. Explain this metric in two lines."
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     max_tokens=50
    # )
    # explanation = response.choices[0].text.strip()
    # return explanation

    url = "https://api.corcel.io/v1/chat/completions"
    
    payload = {
        "model": "llama-3",
        "temperature": 0.1,
        "max_tokens": 500,
        "messages": [
            {
                "role": "user",
                "content": f"The social score of the user is {social_score}. Explain this metric in two lines."
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "e83c689e-e526-4738-996a-f62b5bd5aade"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    return response.text

from web3 import Web3
def send_message_to_contract(loan_id):
    # Initialize the address calling the functions/signing transactions
    caller = web3.eth.account.from_key(PRIVATE_KEY).address
    private_key = PRIVATE_KEY  # To sign the transaction

    # Initialize address nonce
    nonce = web3.eth.get_transaction_count(caller)

    # Create smart contract instance
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    # Initialize the chain id, we need it to build the transaction for replay protection
    chain_id = web3.eth.chain_id

    # Call your function
    call_function = contract.functions.sendMessage(loan_id).buildTransaction({
        'chainId': chain_id,
        'from': caller,
        'nonce': nonce,
    })

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=private_key)


    # Send transaction
    print('Sending transaction...')
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Wait for transaction receipt
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transacion successful")


if __name__ == "__main__":
    vitalik_user_id = '5650'  
    social_score = get_social_score(vitalik_user_id)
    print(f"Social score of user {vitalik_user_id} is {social_score}")
    
    loan_id = 12295443342769835489004685851661808204504702382070150137287530558429035716723
    receipt = send_message_to_contract(loan_id)
    print(f"Transaction receipt: {receipt}")
