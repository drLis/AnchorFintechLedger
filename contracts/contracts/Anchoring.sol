pragma solidity ^0.6.11;


contract Anchoring
{
	constructor() public
	{
		issuer = msg.sender;
	}

	function pushTransfer(bytes32 senderHash, bytes32 receiverHash) external
	{
		require(anchors[senderHash] == 0x00, "Double spending attempt!");
		anchors[senderHash] = receiverHash;
	}

	function computeSenderHash(address sender, uint id) public pure returns (bytes32)
	{
		return keccak256(abi.encodePacked(sender, id));
	}

	function computeReceiverHash(uint id, address receiver) public pure returns (bytes32)
	{
		return keccak256(abi.encodePacked(id, receiver));
	}

	// hash(sender + id) => hash(id + receiver)
	mapping (bytes32 => bytes32) public anchors;

	address public issuer;
}