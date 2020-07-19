pragma solidity ^0.6.11;


contract Anchoring
{
	function push(bytes32 senderHash, bytes32 receiverHash) external
	{
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
}