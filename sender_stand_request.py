import requests

import configuration as conf
import data

def postUser(userData):

    return requests.post(conf.URL_SERVICE + conf.CREATE_USER_PATH,
                         headers = data.headers, 
                         json = userData)

def retrieveAuthToken(response):
    token = response.json()["authToken"]

    return token

def createKitHeader(token):
    header = data.headers.copy()
    header["Authorization"] = f"Bearer {token}"

    return header

def nameKit(name):
    return {"name" : name}

def postNewKit(headers,body):
    return requests.post(conf.URL_SERVICE + conf.KITS_PATH,headers = headers, json = body)

def createKitHeaderHelper(userData):
    return createKitHeader(retrieveAuthToken(postUser(userData)))

def positiveAssert(kit):
    headers = createKitHeaderHelper(data.user)
    response = postNewKit(headers,kit)

    assert response.status_code == 201
    assert response.json()["name"] == kit["name"]

def negativeAssert(kit):
    headers = createKitHeaderHelper(data.user)
    response = postNewKit(headers,kit)

    assert response.status_code == 400
