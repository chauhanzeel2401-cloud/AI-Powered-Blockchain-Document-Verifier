// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DocumentVerifier {
    mapping(bytes32 => bool) public registered;
    event DocumentRegistered(bytes32 indexed docHash, address indexed by, uint256 ts);

    function registerDocument(bytes32 docHash) public {
        require(!registered[docHash], "already registered");
        registered[docHash] = true;
        emit DocumentRegistered(docHash, msg.sender, block.timestamp);
    }

    function verifyDocument(bytes32 docHash) public view returns (bool) {
        return registered[docHash];
    }
}
