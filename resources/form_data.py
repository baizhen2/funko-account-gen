import json
import random

account_data = '{"firstName":"","lastName":"","email":"","password":"","newsletter":true,"accountOrigin":"FUNKO_COM"}'
fanclub_data = '{"email":"","fanClubOptOut":false,"birthMonth":"","birthDay":"","captcharesponse":""}'

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

print(registerFanclub("bob", "hello"))
