def print_all_attr(obj: object):
    type_list = [type(True), type('str'), type(0), type(None), type({'0': 0}), type(0.1), type([])]

    def print_all_attr_copy(obj: object, temp):
        for key in obj.__dict__.keys():
            if temp == 1:
                print(' L  ', end='')
            elif temp == 2:
                print('     L  ', end='')
            elif temp == 3:
                print('         L  ', end='')

            print(key, ': ', end='')

            if type(obj.__getattribute__(key)) in type_list:
                print(obj.__getattribute__(key))
            else:
                print()
                temp += 1
                print_all_attr_copy(obj.__getattribute__(key), temp)
                temp -= 1

    print_all_attr_copy(obj, 0)
    print()

class Address:
    def __init__(self, postal, location):
        self.postal = postal
        self.location = location

class Contact:
    def __init__(self, phone_number, email, adress):
        self.phone_number = phone_number
        self.email = email
        self.adress = adress
class Persona:
    def __init__(self, name: str, age: int, contact: Contact):
        self.name = name
        self.age = age
        self.contact = contact

address = Address('02831','서울시 성북구 성북로4길 52')
contact = Contact('01074334271', 'minimax@snu.ac.kr', address)
persona = Persona('Taegyu Min', 24, contact)

print_all_attr(persona)