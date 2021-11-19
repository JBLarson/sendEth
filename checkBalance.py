#!/usr/bin/python3

import sys
from web3 import Web3
from infuraUrl import infuraUrl

try:
	walletAddress = sys.argv[1]

except:
	walletAddress = '0x2C2E5b824EA2BcE625943aF15e1bBD86630B37EF'




w3 = Web3(Web3.HTTPProvider(infuraUrl))


def fetchETHBalance(walletAddress):
	balanceInWei = w3.eth.getBalance(walletAddress)
	balanceEth = float(Web3.fromWei(balanceInWei, 'ether'))
	addressBalance = {'address': walletAddress, 'balanceEth': balanceEth}
	return addressBalance

checkBalance = fetchETHBalance(walletAddress)


print(checkBalance)


