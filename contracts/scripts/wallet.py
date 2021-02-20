from brownie import *
from brownie import web3
import json
import copy

# Example of banknote
banknote_example = {"info":{"nominal": 100, "id": 1, "issuer": accounts[0].address},
	"indorsement": [[accounts[1].address, "signature1"], [accounts[2].address, "signature2"]]
}

def main():
	print(1)

def issue_banknote(id, nominal, account_issuer, account_target):
	banknote = {}
	banknote["info"] = {}
	banknote["info"]["id"] = id
	banknote["info"]["nominal"] = nominal
	banknote["info"]["issuer"] = account_issuer

	transfer = {'receiver': account_target.address, 'id': id} 
	banknote["indorsement"] = []
	banknote["indorsement"].append([account_target.address, web3.eth.sign(account_issuer.address, text = json.dumps(transfer))])

	return banknote

def transfer_banknote(banknote, receiver):
	new_banknote = copy.deepcopy(banknote)

	transfer = {'receiver': receiver.address, 'id': new_banknote["info"]["id"]}
	owner = banknote["indorsement"][-1][0]
	new_banknote["indorsement"].append([receiver.address, web3.eth.sign(owner, text = json.dumps(transfer))])

	return new_banknote

def validate_banknote(banknote):
	result = False
	anchoring = Anchoring[0]


	return True