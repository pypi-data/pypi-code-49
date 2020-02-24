#!/usr/bin/env python3

from pyteal import *

#template variables
tmpl_fee = Int(Tmpl("TMPL_FEE"))
tmpl_period = Int(Tmpl("TMPL_PERIOD"))
tmpl_dur = Int(Tmpl("TMPL_DUR"))
tmpl_lease = Bytes("base64", Tmpl("TMPL_LEASE"))
tmpl_amt = Int(Tmpl("TMPL_AMT"))
tmpl_rcv = Addr(Tmpl("TMPL_RCV"))
tmpl_timeout = Int(Tmpl("TMPL_TIMEOUT"))

periodic_pay_core = And(Txn.type_enum() == Int(1),
                        Txn.fee() <= tmpl_fee)
                      
periodic_pay_transfer = And(Txn.close_remainder_to() ==  Global.zero_address(),
                            Txn.receiver() == tmpl_rcv,
                            Txn.amount() == tmpl_amt,
                            Txn.first_valid() % tmpl_period == Int(0),
                            Txn.last_valid() == tmpl_dur + Txn.first_valid(),
                            Txn.lease() == tmpl_lease)

periodic_pay_close = And(Txn.close_remainder_to() == tmpl_rcv,
                         Txn.receiver() == Global.zero_address(),
                         Txn.first_valid() >= tmpl_timeout,
                         Txn.amount() == Int(0))

periodic_pay_escrow = And(periodic_pay_core, Or(periodic_pay_transfer, periodic_pay_close))

print(periodic_pay_escrow.teal())
