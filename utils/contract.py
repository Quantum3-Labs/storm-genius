from web3 import Web3
from config.settings import ETH_NODE_URL, CONTRACT_ADDRESS, CONTRACT_ABI, PRIVATE_KEY

web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

def send_message_to_contract(loan_id):
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
    function = contract.functions.sendMessage(loan_id)

    account = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
    nonce = web3.eth.getTransactionCount(account.address)
    gas_price = web3.eth.gasPrice

    transaction = function.buildTransaction({
        'chainId': 696969, 
        'gas': 20000000,
        'gasPrice': gas_price,
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.signTransaction(transaction, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

    return tx_receipt

if __name__ == "__main__":
    loan_id = 12295443342769835489004685851661808204504702382070150137287530558429035716723
    receipt = send_message_to_contract(loan_id)
    print(f"Transaction receipt: {receipt}")
