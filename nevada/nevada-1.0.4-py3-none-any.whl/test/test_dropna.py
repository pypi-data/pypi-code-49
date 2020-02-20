address = {"address":
               {
                   "postal":None,
                    "location":"서울시 성북구 성북로4길 52"
               }
           }

contact={"Contact":
            {
                "phone_number":'01074334271',
                "email":None,
                "address":address
            }
        }
persona = {"persona":
               {"name":'Taegyu Min',
                "age":None,
                "contact":contact
                }
           }

from nevada.Common.Connector import *
print(persona)


# def dropna(input_dict):
#     cleaned_dict = dict()
#     for now in input_dict:
#         if input_dict[now] != None:
#             cleaned_dict.update({now: input_dict[now]})
#     return cleaned_dict

def dropna(input_dict):
    new_dict = dict()
    for key in input_dict:
        if type(input_dict[key]) is dict:
            new_dict[key] = dropna(input_dict[key])
        else:
            if input_dict[key] is not None:
                new_dict[key] = input_dict[key]
    return new_dict

persona = dropna(persona)
print(persona)