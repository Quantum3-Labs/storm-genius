# StormGenius

<h1 align="center">
  <br>
  <img src="stormgenius.png" alt="storm-genius" width="200"></a>
  <br>
Integrating AI for Smarter DeFi Lending Decisions  <br>
</h1>



### Welcome to StormGenius, an innovative project enhancing an existing decentralized lending protocol by leveraging AI technology. Our solution revolutionizes the traditional DeFi protocol by integrating AI, enhancing the credibility assessment process, and providing a more secure and efficient lending experience. Our project exemplifies the potential of AIxWeb3 to transform DeFi by integrating AI for smarter DeFi lending decisions.


### Project Overview
StormGenius operates on top of a decentralized lending protocol involving three key parties:

- Depositor: Deposits cryptocurrency into the protocol.
- Borrower: Requests a loan from the protocol.
- Lender: Assesses the credibility and eligibility of the borrower to decide whether to allocate the loan.

### Features
We introduce two key AI-driven features to enhance the lending process:

#### 1. AI-Powered Borrower Assessment via Galadriel (https://galadriel.com/)

#### Galadriel, a Layer 1 blockchain dedicated to the deployment of AI agents on-chain.

We use the Chatgpt LLM that is integrated into Galadriel to interact with the lending contract to fetch the borrower’s loan-related background. Based on the fetched data, the on-chain Chatgpt LLM provides a credibility assessment and assigns a financial score (0 to 5). This score and assessment help the lender make informed lending decisions.

#### 2. Social Score Assessment via mbd (https://www.mbd.xyz/)

#### mbd offers composable and simple-to-use AI models: Fetches social scores based on interactions on social media platforms like Farcaster or Twitter.

Using mbd to provide the social score of both the borrower and lender is retrieved and assessed.
This social score helps both parties make decisions based on social credibility. Combining financial data and social interactions provides a comprehensive view of the borrower’s credibility and the lender's risk management skills.

## Technologies Used

- **Galadriel**: A Layer 1 blockchain designed for deploying AI agents on-chain.
- **Chatgpt LLM**: An AI model used for interacting with the lending contract and providing financial credibility assessments.
- **mbd API**: Used for fetching social scores based on social media interactions.
- **Python**: The primary programming language used for developing the application.
- **Web3.py**: A Python library for interacting with Ethereum.
- **tkinter**: A standard Python interface to the Tk GUI toolkit used for building the user interface.
- **Social Score Explanation via Corcel** : Corcel allows developers to build with AI, faster, easier and cheaper than ever before. Powered by the Corcel API, developers can release the full potential of what they can do with decentralized machine learning. After getting the social score, we prompt a large language model to give a personalized explanation of the score. 


## How It Works

### Financial Score

1. **Smart Contract Interaction**: The application interacts with a smart contract deployed on the Galadriel blockchain.
2. **Data Fetching**: The smart contract fetches the borrower’s loan-related background data.
3. **AI Assessment**: The fetched data is sent to the on-chain Chatgpt LLM, which processes the data and returns a credibility assessment.
4. **Score Assignment**: The Chatgpt LLM assigns a financial score (0 to 5) based on the borrower's historical loan repayment behavior.
5. **Result Display**: The financial score and the detailed assessment are displayed to the lender.

### Social Score

1. **User Input**: The lender provides the Farcaster ID of the borrower.
2. **Data Fetching**: The application uses the mbd API to fetch recent social interactions and sentiment data related to the borrower.
3. **AI Analysis**: The fetched data is analyzed to determine the trust level based on social interactions.
4. **Score Calculation**: The social score is calculated based on the average trust level from the interactions.
5. **Result Display**: The social score is displayed to the lender, providing additional context to the borrower's credibility.

By leveraging AI models on-chain and fetching real-time social interaction data, StormGenius provides a comprehensive and robust assessment of a borrower's credibility, enhancing the overall security and efficiency of the decentralized lending process.

## How to Run the Script

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed on your machine.
2. **Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Quantum3-Labs/storm-genius.git
    cd storm-genius
    ```

2. **Create and Activate Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **API Keys and Settings**: Update the `config/settings.py` file with your API keys and other settings:
    ```python
    # config/settings.py

    API_BASE_URL = 'https://api.example.com'
    PRIVATE_KEY='your_private_key_here'

    # MBD API Key
    MBD_API_KEY = 'your_mbd_api_key_here'

    # Ethereum node and contract configuration
    ETH_NODE_URL = 'https://devnet.galadriel.com/'
    CONTRACT_ADDRESS = '0xC5e3F849996167E80CB7B224696dcAEA6e35F0C1'
    CONTRACT_ABI = [...]
    ```

### Running the Script

1. **Run the Application**:
    ```bash
    python3 app.py
    ```

### Usage

1. **Start the Application**: When you run the script, a GUI will appear with an image of StormGenius.
2. **Choose Score Type**: Select whether you want to fetch a social score or a financial score.
3. **Enter Required Information**: Depending on your choice, enter the Farcaster ID or Loan ID when prompted.
4. **View Results**: The application will fetch and display the relevant score and assessment.

By following these steps, you can easily run the StormGenius bot and leverage its capabilities to assess borrower credibility in a decentralized lending protocol.

## Contracts

- **ChatgptLLM**: [0xC5e3F849996167E80CB7B224696dcAEA6e35F0C1](https://explorer.galadriel.com/address/0xC5e3F849996167E80CB7B224696dcAEA6e35F0C1)
- **LoanManager (from Lending protocol)**: 0x5BB7839f554da657e80C19998Fa685Fd28B9697F

### To deploy ChatgptLLM contract:

```bash
forge script script/DeployChatgptLLM.s.sol --rpc-url $GALADRIEL_RPC_URL --private-key $PRIVATE_KEY --legacy --broadcast