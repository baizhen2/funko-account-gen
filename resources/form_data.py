import json

data = '{"firstName":"","lastName":"","email":"","password":"","newsletter":true,"accountOrigin":"FUNKO_COM"}'

def fillAccForm(firstName, lastName, email, password):
    parsed = json.loads(data)
    parsed["firstName"] = firstName
    parsed["lastName"] = lastName
    parsed["email"] = email
    parsed["password"] = password

    json_string = json.dumps(parsed)
    return json_string





    


