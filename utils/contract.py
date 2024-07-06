from web3 import Web3
from config.settings import ETH_NODE_URL, CONTRACT_ADDRESS, CONTRACT_ABI

web3 = Web3(Web3.HTTPProvider(ETH_NODE_URL))

def get_contract_data(contract_address, abi, function_name, *args):
    contract = web3.eth.contract(address=contract_address, abi=abi)
    function = contract.functions[function_name](*args)
    return function.call()
