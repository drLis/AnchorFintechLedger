from brownie import *
import pytest


def test_push(accounts, test):
	def transfer(sender, receiver, id):
		sender_hash = test.computeSenderHash(accounts[0], id)
		receiver_hash = test.computeReceiverHash(id, accounts[1])
		test.push(sender_hash, receiver_hash)
	
	def check_transfer(sender, receiver, id):
		sender_hash = test.computeSenderHash(accounts[0], id)
		receiver_hash = test.computeReceiverHash(id, accounts[1])
		return test.anchors(sender_hash) == receiver_hash
	
	transfer(accounts[0], accounts[1], 1)
	assert check_transfer(accounts[0], accounts[1], 1)
	transfer(accounts[1], accounts[2], 1)
	assert check_transfer(accounts[1], accounts[2], 1)