# API configuration
API_BASE_URL = 'https://api.example.com'
PRIVATE_KEY=''

# MBD API Key
MBD_API_KEY = 'mbd-874407afb51a3cd56c8ae0b22d73156eb0284033edd075fea27b249275c5c21b'

# Ethereum node and contract configuration
ETH_NODE_URL = 'https://devnet.galadriel.com/'
CONTRACT_ADDRESS='0xAEe9Fe4A23B40e02d44DF0467AEa2e0235650fe0'
CONTRACT_ABI = [
    {"type":"constructor","inputs":[{"name":"initialOracleAddress","type":"address","internalType":"address"},{"name":"loanManagerAddr","type":"address","internalType":"address"},{"name":"_contextPrompt","type":"string","internalType":"string"}],"stateMutability":"nonpayable"},
    {"type":"function","name":"contextPrompt","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},
    {"type":"function","name":"getMessageHistory","inputs":[{"name":"","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"tuple[]","internalType":"struct IOracle.Message[]","components":[{"name":"role","type":"string","internalType":"string"},{"name":"content","type":"tuple[]","internalType":"struct IOracle.Content[]","components":[{"name":"contentType","type":"string","internalType":"string"},{"name":"value","type":"string","internalType":"string"}]}]}],"stateMutability":"view"},
    {"type":"function","name":"messages","inputs":[{"name":"","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"role","type":"string","internalType":"string"}],"stateMutability":"view"},
    {"type":"function","name":"onOracleOpenAiLlmResponse","inputs":[{"name":"","type":"uint256","internalType":"uint256"},{"name":"_response","type":"tuple","internalType":"struct IOracle.OpenAiResponse","components":[{"name":"id","type":"string","internalType":"string"},{"name":"content","type":"string","internalType":"string"},{"name":"functionName","type":"string","internalType":"string"},{"name":"functionArguments","type":"string","internalType":"string"},{"name":"created","type":"uint64","internalType":"uint64"},{"name":"model","type":"string","internalType":"string"},{"name":"systemFingerprint","type":"string","internalType":"string"},{"name":"object","type":"string","internalType":"string"},{"name":"completionTokens","type":"uint32","internalType":"uint32"},{"name":"promptTokens","type":"uint32","internalType":"uint32"},{"name":"totalTokens","type":"uint32","internalType":"uint32"}]},{"name":"_errorMessage","type":"string","internalType":"string"}],"outputs":[],"stateMutability":"nonpayable"},
    {"type":"function","name":"response","inputs":[],"outputs":[{"name":"","type":"string","internalType":"string"}],"stateMutability":"view"},
    {"type":"function","name":"sendMessage","inputs":[{"name":"loanId","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"}
]
