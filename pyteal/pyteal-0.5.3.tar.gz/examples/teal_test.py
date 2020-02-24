import params, base64
from algosdk import algod, transaction, account, mnemonic

# create algod clients
acl = algod.AlgodClient(params.algod_token, params.algod_address)

# create logic sig
program = base64.b64decode("ASAHAegHMgCIJ9APsOoBJgIG023sdDE2IM5AXoIg4wguvqNz/cSzrushKftw0p2NFXgq73Ht5ZNSMRAiEjEBIw4QMQIkGCUSEDEEIQQxAggSEDEGKBIQMQkyAxIxBykSEDEIIQUSEDEJKRIxBzIDEhAxAiEGEhAxCCUSEBEQ")
lsig = transaction.LogicSig(program)

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
startRound = params.lastRound - (params.lastRound % 50)
endRound = startRound + 1000
fee = 0
amount = 2000
receiver = "ZZAF5ARA4MEC5PVDOP64JM5O5MQST63Q2KOY2FLYFLXXD3PFSNJJBYAFZM"

# create a transaction
txn = transaction.PaymentTxn(addr, fee, startRound, endRound, gh, receiver, amount)
# Create the LogicSigTransaction with contract account LogicSig
lstx = transaction.LogicSigTransaction(txn, lsig)

# send raw LogicSigTransaction to network
txid = acl.send_transaction(lstx)
print("Transaction ID: " + txid)
