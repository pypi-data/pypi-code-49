import os
from unifiedAPI import saleQR

#Payment Type
QR = 1
Credit = 2
EPS = 3
Octopus = 4
EXIT = 5


#Transaction Type of QR
SALE = 1
VOID = 2
REFUND = 3
RETRIV = 4

transData = {}
printReceipt = []

while True:
    print("Payment Type :")
    print("1. QR\n2. Credit Card\n3. EPS\n4. Octopus\n5. EXIT" )

    paymentType = int(input("Enter the Payment type:\n"))

    if paymentType == EXIT:
        break

    print("Transaction Type:" )
    print("1. Sale\n2. Void\n3. Refund\n" )
    txnType = int(input("Enter the Transaction type:\n"))

    if paymentType == QR:
        if txnType == SALE:
            amount = input("INPUT AMOUNT:\n")
            qrCode = input("INPUT QR CODE:\n")
            ecrRef = input("INPUT ECR REF:\n")
            #Call middle Layer
            result = saleQR("QR",qrCode,ecrRef,amount,0,"","",transData,printReceipt)

            #Complete Call
            print("SALE Result:"+ str(result)+"\n")
            print("Receipt:\n")
            for val in printReceipt:
                print(val+"\n")

        elif txnType == VOID:
            invoice = input("INPUT INVOICE or TRACE:\n")
            #Call middle Layer

        elif txnType == REFUND:
            amount = input("INPUT AMOUNT:\n")
            ecrRef = input("INPUT ECR REF:\n")
            oriData = input("INPUT ORIGINAL DATA:\n")
            #Call middle




