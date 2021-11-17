#!/usr/bin/python3



from web3 import Web3
from infuraUrl import infuraUrl
import os
import time


w3 = Web3(Web3.HTTPProvider(infuraUrl))


testingWallet0 = '0xc838C62098f8C4597908BE707130F63eCeC2ffB7'
testingWallet1 = '0x2C2E5b824EA2BcE625943aF15e1bBD86630B37EF'



def fetchETHBalance(walletAddress):
	balanceInWei = w3.eth.getBalance(walletAddress)
	balanceEth = float(Web3.fromWei(balanceInWei, 'ether'))
	addressBalance = {'address': walletAddress, 'balanceEth': balanceEth}
	return addressBalance


fetchWallet0, fetchWallet1 = fetchETHBalance(testingWallet0), fetchETHBalance(testingWallet1)

print("\nWallet balances before sending")
print(fetchWallet0)
print(fetchWallet1)






def sendEther(address0, address1, address0pKey, etherAmount):

	nonce = w3.eth.getTransactionCount(address0)
	tx = {'nonce': nonce,
		  'to': address1,
		  'value': w3.toWei(etherAmount, 'ether'),
		  'gas': 21000,
		  'gasPrice': w3.toWei(40, 'gwei'),
		  }
	signedTx = w3.eth.account.signTransaction(tx, address0pKey)

	tx_hash = w3.eth.sendRawTransaction(signedTx.rawTransaction)

	return tx


# private key for wallet 0
privateKey = os.getenv('privateKey')



sendTest = sendEther(testingWallet0, testingWallet1, privateKey, 1)

# wait 20 seconds and check wallet balances again
time.sleep(20)

fetchWallet0, fetchWallet1 = fetchETHBalance(testingWallet0), fetchETHBalance(testingWallet1)

print("\nWallet balances after sending")
print(fetchWallet0)
print(fetchWallet1)






