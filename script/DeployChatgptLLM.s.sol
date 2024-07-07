// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.21;

import {Script, console} from "forge-std/Script.sol";
import {DeployHelpers} from "./DeployHelpers.s.sol";
import {ChatgptLLM} from "../src/llm/ChatgptLLM.sol";

contract DeployChatgptLLM is DeployHelpers {
    address constant ORACLE_ADDRESS =
        0x68EC9556830AD097D661Df2557FBCeC166a0A075;
    address constant LOAN_MANAGER_ADDRESS =
        0x5BB7839f554da657e80C19998Fa685Fd28B9697F;

    string constant CONTEXT_PROMPT =
        "You act as a financial assistant. You will receive data from another smart contract related to the loan data of a specific borrower. You need to asset based on this data the credibility and the eligibility of the borrower for a new loan. You will finally return me a socre from 0 to 5 to let the lender know if the borrower is eligible for a new loan. Please begin your reponse by repeating the user prompt that you received and following by this format: {This is my assessment result: }";

    function run() public returns (ChatgptLLM) {
        vm.startBroadcast();

        ChatgptLLM chatgptLLM = new ChatgptLLM(
            ORACLE_ADDRESS,
            LOAN_MANAGER_ADDRESS,
            CONTEXT_PROMPT
        );

        vm.stopBroadcast();

        return chatgptLLM;
    }
}
