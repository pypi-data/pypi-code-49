import re

from klotan.criteria.core import fn_to_criteria

# These criteria are for example purposes only !

_country2length = dict(
    AL=28, AD=24, AT=20, AZ=28, BE=16, BH=22, BA=20, BR=29,
    BG=22, CR=21, HR=21, CY=28, CZ=24, DK=18, DO=28, EE=20,
    FO=18, FI=18, FR=27, GE=22, DE=22, GI=23, GR=27, GL=18,
    GT=28, HU=28, IS=26, IE=22, IL=23, IT=27, KZ=20, KW=30,
    LV=21, LB=28, LI=21, LT=20, LU=20, MK=19, MT=31, MR=27,
    MU=30, MC=27, MD=24, ME=22, NL=18, NO=15, PK=24, PS=29,
    PL=28, PT=25, RO=24, SM=27, SA=24, RS=22, SK=24, SI=19,
    ES=24, SE=24, CH=21, TN=24, TR=26, AE=23, GB=22, VG=24 )

@fn_to_criteria
def is_valid_iban():
    def valid_iban_wrapper(iban):
        iban = iban.replace(' ','').replace('\t','')
        if not re.match(r'^[\dA-Z]+$', iban):
            return False
        if len(iban) != _country2length[iban[:2]]:
            return False
        iban = iban[4:] + iban[:4]
        digits = int(''.join(str(int(ch, 36)) for ch in iban)) #BASE 36: 0..9,A..Z -> 0..35
        return digits % 97 == 1
    return valid_iban_wrapper

@fn_to_criteria
def is_valid_credit_card_number():
    def is_valid_credit_card_number_wrapper(cc_num):
        cc_num = cc_num[::-1]
        cc_num = [int(x) for x in cc_num]
        doubled_second_digit_list = list()
        digits = list(enumerate(cc_num, start=1))
        for index, digit in digits:
            if index % 2 == 0:
                doubled_second_digit_list.append(digit * 2)
            else:
                doubled_second_digit_list.append(digit)
        doubled_second_digit_list = [
            x if x < 10 else ((x % 10) + (x // 10))
            for x in doubled_second_digit_list
        ]
        sum_of_digits = sum(doubled_second_digit_list)
        return sum_of_digits % 10 == 0
    return is_valid_credit_card_number_wrapper