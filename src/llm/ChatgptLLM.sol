// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

import "../interfaces/IOracle.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import {ILoanManager} from "../interfaces/managers/loan/ILoanManager.sol";

contract ChatgptLLM {
    ILoanManager private loanManager;

    address private oracleAddress; // use latest: https://docs.galadriel.com/oracle-address
    // IOracle.Message public message;
    IOracle.Message[] public messages;
    string public response;
    IOracle.OpenAiRequest private config;
    string public contextPrompt;

    constructor(
        address initialOracleAddress,
        address loanManagerAddr,
        string memory _contextPrompt
    ) {
        oracleAddress = initialOracleAddress;
        contextPrompt = _contextPrompt;
        loanManager = ILoanManager(loanManagerAddr);

        config = IOracle.OpenAiRequest({
            model: "gpt-4-turbo", // gpt-4-turbo gpt-4o
            frequencyPenalty: 21, // > 20 for null
            logitBias: "", // empty str for null
            maxTokens: 1000, // 0 for null
            presencePenalty: 21, // > 20 for null
            responseFormat: '{"type":"text"}',
            seed: 0, // null
            stop: "", // null
            temperature: 10, // Example temperature (scaled up, 10 means 1.0), > 20 means null
            topP: 101, // Percentage 0-100, > 100 means null
            tools: "",
            toolChoice: "", // "none" or "auto"
            user: "" // null
        });
    }

    function sendMessage(uint256 loanId) public {
        ILoanManager.Loan memory loan = loanManager.getLoan(loanId);
        uint256 assetsAllocated = loan.assetsAllocated;
        // ILoanManager.LoanStatus status = loan.status;

        string memory assetsAllocatedString = Strings.toString(assetsAllocated);
        // string memory statusString = Strings.toString(uint256(status));
        string memory promptMessage = string(
            abi.encodePacked(
                "The borrower has the following loan-related background: the borrower has borrowed 5 times in the past 2 years ",
                assetsAllocatedString,
                " of crypto. All these loans have the status of paid with delay. Based on this data, please provide the borrower's eligibility score to the lender."
            )
        );
        messages = createTextMessage("user", promptMessage);
        IOracle(oracleAddress).createOpenAiLlmCall(0, config);
    }

    // required for Oracle
    function onOracleOpenAiLlmResponse(
        uint /*runId*/,
        IOracle.OpenAiResponse memory _response,
        string memory _errorMessage
    ) public {
        require(msg.sender == oracleAddress, "Caller is not oracle");
        if (bytes(_errorMessage).length > 0) {
            response = _errorMessage;
        } else {
            response = _response.content;
        }
    }

    // required for Oracle
    function getMessageHistory(
        uint /*_runId*/
    ) public view returns (IOracle.Message[] memory) {
        IOracle.Message[] memory theMessages = new IOracle.Message[](2);
        theMessages[0] = messages[0];
        theMessages[1] = messages[1];
        return theMessages;
    }

    // @notice Creates a text message with the given role and content
    // @param role The role of the message
    // @param content The content of the message
    // @return The created message
    function createTextMessage(
        string memory role,
        string memory content
    ) private returns (IOracle.Message[] memory) {
        IOracle.Message memory systemMessage = IOracle.Message({
            role: "system",
            content: new IOracle.Content[](1)
        });
        systemMessage.content[0].contentType = "text";
        systemMessage.content[0].value = contextPrompt;
        messages.push(systemMessage);

        IOracle.Message memory newMessage = IOracle.Message({
            role: role,
            content: new IOracle.Content[](1)
        });
        newMessage.content[0].contentType = "text";
        newMessage.content[0].value = content;
        messages.push(newMessage);

        return messages;
    }
}
