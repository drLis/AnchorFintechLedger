from brownie import *

def main():
	contract = accounts[0].deploy(Anchoring)
	return contract.contract_address