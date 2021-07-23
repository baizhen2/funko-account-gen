import json
import random

account_data = '{"firstName":"","lastName":"","email":"","password":"","newsletter":true,"accountOrigin":"FUNKO_COM"}'
fanclub_data = '{"email":"","fanClubOptOut":false,"birthMonth":"","birthDay":"","captcharesponse":""}'
auth_data = '{"email":"","password":"","returnSecureToken":true}'
auth_params = (
    ('key', 'AIzaSyAxsxYDhfpn5yCkpNVQid2K116UmYvUCAk'), #Funko's google api-key for login auth-tokens, they make it too easy to find... Anyone is free to use it ;)
)
address_data = '{"country":"US","isDefault":true,"firstName":"","lastName":"","line1":"","city":"","state":"","zip":""}'

def fillAccForm(firstName, lastName, email, password):
    parsed = json.loads(account_data)
    parsed["firstName"] = firstName
    parsed["lastName"] = lastName
    parsed["email"] = email
    parsed["password"] = password

    json_string = json.dumps(parsed)
    return json_string

def registerFanclub(email, captchaToken):
    parsed = json.loads(fanclub_data)
    
    parsed["email"] = email
    parsed["captcharesponse"] = captchaToken
    parsed["birthMonth"] = str(random.randint(2,9)) #Don't want to handle edge cases
    parsed["birthDay"] = str(random.randint(2,25))

    json_string = json.dumps(parsed)
    return json_string

def fillAuthData(email, password):
    parsed = json.loads(auth_data)
    
    parsed["email"] = email
    parsed["password"] = password

    json_string = json.dumps(parsed)
    return json_string

def fillAddressInfo(firstName, lastName, addressLineOne, city, state, zip):
    parsed = json.loads(address_data)
    parsed["firstName"] = firstName
    parsed["lastName"] = lastName
    parsed["line1"] = addressLineOne
    parsed["city"] = city
    parsed["state"] = state
    parsed["zip"] = zip

    json_string = json.dumps(parsed)
    return json_string