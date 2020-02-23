class BillData(object):

    def __init__(self):

        self.bits = 10
        self.last_bit_farm = None

        self.debit = []
        self.credit = []
        self.transfers = []
        self.spent = 0
        self.given = 0

    def extract_data(self, raw_data):
        self.bits = raw_data.get('bits', self.bits)
        self.last_bit_farm = raw_data.get('last_bit_farm', self.last_bit_farm)

        return self

    def build_data(self):

        data_out = {
            'bits': self.bits,
            'last_bit_farm': self.last_bit_farm
        }

        return data_out
