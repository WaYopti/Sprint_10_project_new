import requests
import config
import data
import helper


def create_booking(body):
    return requests.post(url=config.URL + config.CREATE, json=body)

def delete_booking(booking_id):
    header = data.header_delete
    header['Cookie'] = "token=" + get_token()
    return requests.delete(config.URL + config.DELETE + str(booking_id), headers=header)

def get_token():
    responce = requests.post(url=config.URL + config.AUTH, json=data.body_auth)
    token = responce.json()['token']
    return token

# первый тест
#body_test = data.body_create.copy() - при создании файла хелпер, эти строки удаляются
#body_test["firstname"] = 'fff'
body = helper.change_body_create("Jjjjj")
responce = create_booking(body).status_code
# print(create_booking(body_test).status_code)
print(responce)

# 2 тест
#body_test = data.body_create.copy()
#body_test["firstname"] = 'fff'
body = helper.change_body_create("Jjjjj")
responce = create_booking(body).status_code
# print(create_booking(body_test).status_code)
print(responce)
