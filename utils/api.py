import json
import requests
import openai
from config.settings import API_BASE_URL, MBD_API_KEY, ETH_NODE_URL, PRIVATE_KEY
from web3 import Web3

# Connect to the network
web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

# Verify if the connection is successful
if web3.is_connected():
    print("-" * 50)
    print("Connection Successful")
    print("-" * 50)
else:
    raise Exception("Connection Failed")

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

def send_message_to_contract(loan_id):
    abi = json.loads('[{"type":"constructor","inputs":[{"name":"initialOracleAddress","type":"address","internalType":"address"},{"name":"loanManagerAddr","type":"address","internalType":"address"},{"name":"_contextPrompt","type":"string","internalType":"string"}],"stateMutability":"nonpayable"},{"type":"function","name":"contextPrompt","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"getMessageHistory","inputs":[{"name":"","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"tuple[]","internalType":"struct IOracle.Message[]","components":[{"name":"role","type":"string","internalType":"string"},{"name":"content","type":"tuple[]","internalType":"struct IOracle.Content[]","components":[{"name":"contentType","type":"string","internalType":"string"},{"name":"value","type":"string","internalType":"string"}]}]}],"stateMutability":"view"},{"type":"function","name":"messages","inputs":[{"name":"","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"role","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"onOracleOpenAiLlmResponse","inputs":[{"name":"","type":"uint256","internalType":"uint256"},{"name":"_response","type":"tuple","internalType":"struct IOracle.OpenAiResponse","components":[{"name":"id","type":"string","internalType":"string"},{"name":"content","type":"string","internalType":"string"},{"name":"functionName","type":"string","internalType":"string"},{"name":"functionArguments","type":"string","internalType":"string"},{"name":"created","type":"uint64","internalType":"uint64"},{"name":"model","type":"string","internalType":"string"},{"name":"systemFingerprint","type":"string","internalType":"string"},{"name":"object","type":"string","internalType":"string"},{"name":"completionTokens","type":"uint32","internalType":"uint32"},{"name":"promptTokens","type":"uint32","internalType":"uint32"},{"name":"totalTokens","type":"uint32","internalType":"uint32"}]},{"name":"_errorMessage","type":"string","internalType":"string"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"response","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},{"type":"function","name":"sendMessage","inputs":[{"name":"loanId","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"}]')
    contract_address = '0xAEe9Fe4A23B40e02d44DF0467AEa2e0235650fe0'

    # Initialize the address calling the functions/signing transactions
    caller = web3.eth.account.from_key(PRIVATE_KEY).address
    private_key = PRIVATE_KEY  # To sign the transaction

    # Initialize address nonce
    nonce = web3.eth.get_transaction_count(caller)

    # Create smart contract instance
    contract = web3.eth.contract(address=contract_address, abi=abi)
    print("Contract instance created", contract)

    # Initialize the chain id, we need it to build the transaction for replay protection
    chain_id = web3.eth.chain_id

    # Call your function
    call_function = contract.functions.sendMessage(loan_id).build_transaction({
        'chainId': 696969,
        'from': caller,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.to_wei('5', 'gwei')
    })

    # Sign transaction
    signed_tx = web3.eth.account.sign_transaction(call_function, private_key=private_key)

    # Send transaction
    print('Sending transaction...')
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    # Wait for transaction receipt
    print("Waiting for transaction receipt...")
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction successful")

    return tx_receipt

if __name__ == "__main__":
    vitalik_user_id = '5650'  
    social_score = get_social_score(vitalik_user_id)
    print(f"Social score of user {vitalik_user_id} is {social_score}")
    
    loan_id = 12295443342769835489004685851661808204504702382070150137287530558429035716723
    receipt = send_message_to_contract(loan_id)
    print(f"Transaction receipt: {receipt}")
