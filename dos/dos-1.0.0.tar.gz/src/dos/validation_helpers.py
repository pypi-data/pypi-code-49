import re


# source: http://rion.io/2013/09/10/validating-social-security-numbers-through-regular-expressions-2/
def validate_social_security_number(potential_social_security_number):
    if not isinstance(potential_social_security_number, str):
        potential_social_security_number = str(potential_social_security_number)

    if re.match(r'^(?!219099999|078051120)(?!666|000|9\d{2})\d{3}(?!00)\d{2}(?!0{4})\d{4}$', potential_social_security_number):
        return True

    return False
