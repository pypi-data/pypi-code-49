import base64
from algosdk import algod, transaction, account, mnemonic

# create algod clients
# acl = algod.AlgodClient(params.algod_token, params.algod_address)

# create an algod client
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
acl = algod.AlgodClient(algod_token, algod_address)

# try:

# create logic sig
# hex example b"\x01\x20\x01\x00\x22" 
program = base64.b64decode("ASAGAegHMgDQD7DqASYCIMvTieTESwh0I/Bqm4pAFCjASO4aJvkjo/HZaKTXTR1yIM5AXoIg4wguvqNz/cSzrushKftw0p2NFXgq73Ht5ZNSMRAiEjEBIw4QMQIkGCUSEDEEIzECCBIQMQYoEhAxCTIDEjEHKRIQMQghBBIQMQkpEjEHMgMSEDECIQUSEDEIJRIQERA=")
# program = ("b\x01\x20\x01\x00\x22")
lsig = transaction.LogicSig(program)
sender = lsig.address()

#Recover the account that is wanting to delegate signature
passphrase = "patrol crawl rule faculty enemy sick reveal embody trumpet win shy zero ill draw swim excuse tongue under exact baby moral kite spring absent double"
sk = mnemonic.to_private_key(passphrase)
addr = account.address_from_private_key(sk)
print( "Address of Sender/Delgator: " + addr )

# sign the logic signature with an account sk
lsig.sign(sk)

# get suggested parameters
params = acl.suggested_params()
gen = params["genesisID"]
gh = params["genesishashb64"]
startRound = params["lastRound"] - (params["lastRound"] % 50)
endRound = startRound + 1000
fee = 0
amount = 2000
receiver = "ZZAF5ARA4MEC5PVDOP64JM5O5MQST63Q2KOY2FLYFLXXD3PFSNJJBYAFZM"
lease = base64.b64decode("y9OJ5MRLCHQj8GqbikAUKMBI7hom+SOj8dlopNdNHXI=")

# create a transaction
txn = transaction.PaymentTxn(addr, fee, startRound, endRound, gh, receiver, amount, flat_fee=False, lease=lease)

# Create the LogicSigTransaction with contract account LogicSig
lstx = transaction.LogicSigTransaction(txn, lsig)

# send raw LogicSigTransaction to network
txid = acl.send_transaction(lstx)
print("Transaction ID: " + txid )
# except Exception as e:
#     print(e)    
