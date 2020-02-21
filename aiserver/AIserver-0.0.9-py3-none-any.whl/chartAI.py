import json
import requests


def postChat(txet_data, user_number):
    url_json = 'https://ai.herunlei.com:8090/chatAI'
    data_json = json.dumps({'code': 3, 'user': user_number, 'text': txet_data})
    headers = {'content-type': 'application/json;charset=UTF-8'}
    r_json = requests.post(url_json, data_json, headers=headers)
    res = r_json.json()
    answer = res['data']
    return answer


def run(APIkey):
    while True:
        try:
            request = input(">>")
            response = postChat(request, APIkey)
            print("the AI said:", response)
        except:
            print("AI开小差了呢>0<")



