# StormGenius

<h1 align="center">
  <br>
  <img src="stormgenius.png" alt="storm-genius" width="200"></a>
  <br>
  An AI tool leveraging Graph Neural Networks (GNNs)
  <br>
</h1>

### Welcome to StormGenius, an innovative project enhancing an existing decentralized lending protocol by leveraging AI technology. Our solution revolutionizes the traditional DeFi protocol by integrating AI, enhancing the credibility assessment process, and providing a more secure and efficient lending experience. Our project exemplifies the potential of AIxWeb3 to transform DeFi.

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
