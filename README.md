# web3
Simple scripts for using python's web3 library

1. Create and activate a virtual environment
 - >> python3 -m venv web3Env
 - >> source web3Env/bin/activate

2. Install requirements
 - >> pip3 install -r req.txt
 
3. Add the URL for your infura endpoint to [infuraUrl.py](infuraUrl.py)
4. Add your private key as an environment variable.
 - >> export privateKey=the-private-key-for-your-wallet
5. Change the wallet addresses in [sendEth.py](sendEth.py) to your own wallets.
6. Run the script
 - >> python3 sendEth.py
