// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

//Import OpenZeppelin ERC-20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

//CatCoin token contract inheriting ERC-20 standard
contract CatCoin is ERC20 {

    //Constructor runs once at deployment
    constructor() ERC20("CatCoin", "CAT") {

        //Mint 20 tokens to deployer address
        //decimals() = 18 for ERC-20 
        _mint(msg.sender, 20 * 10 ** decimals());
    }
}
