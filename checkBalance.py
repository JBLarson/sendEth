#!/usr/bin/python3

import sys
from web3 import Web3
from infuraUrl import infuraUrl


walletAddress = sys.argv[1]



w3 = Web3(Web3.HTTPProvider(infuraUrl))


def fetchETHBalance(walletAddress):
	balanceInWei = w3.eth.getBalance(walletAddress)
	balanceEth = float(Web3.fromWei(balanceInWei, 'ether'))
	addressBalance = {'address': walletAddress, 'balanceEth': balanceEth}
	return addressBalance

checkBalance = fetchETHBalance(walletAddress)


print(checkBalance)
