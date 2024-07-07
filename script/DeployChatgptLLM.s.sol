// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.21;

import {Script, console} from "forge-std/Script.sol";
import {DeployHelpers} from "./DeployHelpers.s.sol";
import {ChatgptLLM} from "../src/llm/ChatgptLLM.sol";

contract DeployChatgptLLM is DeployHelpers {
    address constant ORACLE_ADDRESS =
        0x68EC9556830AD097D661Df2557FBCeC166a0A075;
    address constant LOAN_MANAGER_ADDRESS =
        0x31d45DAa525bb85F200E65390A5685B9253f5006;

    string constant CONTEXT_PROMPT =
        "You are an impartial financial assistant. You will help me analyze the borrower's eligibility to borrow a loan. Based on the elements and data provided, you will return me a score from 0 to 5 points so that we know the level of credibility of the borrower. The lender will decide to borrow or not based on your score.";

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
