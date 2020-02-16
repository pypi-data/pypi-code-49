#!/usr/bin/env python3


from importlib import import_module


# Available crypto currency's
available_currency = [
    "bitcoin",
    "bytom"
]


class CryptoCurrency:

    def __init__(self, currency):
        if currency in available_currency:
            # Initialization shuttle swap
            self.Wallet = getattr(import_module(".providers.%s.wallet" % currency), 'Wallet')
            self.HTLC = getattr(import_module(".providers.%s.htlc" % currency), 'HTLC')
            self.FundTransaction = getattr(import_module(".providers.%s.transaction" % currency), 'FundTransaction')
            self.ClaimTransaction = getattr(import_module(".providers.%s.transaction" % currency), 'ClaimTransaction')
            self.RefundTransaction = getattr(import_module(".providers.%s.transaction" % currency), 'RefundTransaction')
            self.FundSolver = getattr(import_module(".providers.%s.solver" % currency), 'FundSolver')
            self.ClaimSolver = getattr(import_module(".providers.%s.solver" % currency), 'ClaimSolver')
            self.RefundSolver = getattr(import_module(".providers.%s.solver" % currency), 'RefundSolver')
        else:
            raise NameError("Invalid crypto currency.")

    def htlc(self):
        pass

    def fund(self):
        pass

    def claim(self):
        pass

    def refund(self):
        pass

    def sign(self):
        pass


