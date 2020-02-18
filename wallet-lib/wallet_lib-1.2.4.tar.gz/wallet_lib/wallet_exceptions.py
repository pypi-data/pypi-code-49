class WalletException(Exception):

    def __init__(self, reason, code):
        self.reason = reason
        self.code = code
        super().__init__(reason)

class WalletInputException(WalletException):

    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason, -901)

class WalletIsNotSupportedException(WalletException):
    
    def __init__(self, ticker_symbol):
        super().__init__('{} wallet is not supported'.format(ticker_symbol), -902)
