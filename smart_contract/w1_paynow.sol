// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract weixin{
    address payer;
    address payee;
    uint amount;

    function transfer_money(address payer_input, address payee_input, uint amount_input) public{
        payer = payer_input;
        payee = payee_input;
        amount = amount_input;


    }

    function transfer_view() public view returns (address, address, uint){
        return(payer, payee, amount);
    }

}

