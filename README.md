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

We use the Chatgpt LLM that is integrated into Galadriel to interact with the lending contract to fetch the borrower’s loan-related background. Based on the fetached data, the onchain Chatgpt LLM provides a credibility assessment and assigns a financial score (0 to 5). This score and assessment help the lender make informed lending decisions.

#### 2. Social Score Assessment via mbd (https://www.mbd.xyz/)

#### mdb offers composable and simple to use AI models: Fetches social scores based on interactions on social media platforms like Farcaster or Twitter.

Using mdb to provide the social score of both the borrower and lender is retrieved and assessed.
This social score helps both parties make decisions based on social credibility. Combining financial data and social interactions provides a comprehensive view of the borrower’s credibility and the lender of risk managing skills.