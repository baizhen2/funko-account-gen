import requests
import names
import json
import address
from resources import headers, form_data

class Task:

    def __init__(self, email, password, proxy):
        self.email = email
        self.password = password #password created from task engine
        self.proxy = proxy #proxyDict formatted from task engine

        self.session = requests.Session()
        self.firstName = None
        self.lastName = None

    def proxySetup(self):
        self.session.proxies.update(self.proxy)

    def accountFormSetup(self):
        self.firstName = names.get_first_name()
        self.lastName = names.get_last_name()

        return form_data.fillAccForm(
            self.firstName,
            self.lastName,
            self.email,
            self.password
        )

    def registerFormSetup(self, captchaToken):
        return form_data.registerFanclub(self.email, captchaToken)

    def generateAccount(self):
        self.proxySetup()
        data = self.accountFormSetup()

        response = self.session.post('https://www.funko.com/api/users/signup', headers=headers.create_acc_headers, data=data)

        if response.status_code != 200:
            print("Account creation failed")
            return False

        else:
            print("Account created")
            return True
        
    def getAuthToken(self):
        data = form_data.fillAuthData(self.email, self.password)

        response = self.session.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword',
                            headers=headers.authorization_headers,
                            params=form_data.auth_params,
                            data=data)
        data = json.loads(response.text)
        return data["idToken"]
    
    def signupFanclub(self, captchaToken):
        data = self.registerFormSetup(captchaToken)
        self.getAuthToken()

        fanclub_headers = headers.fanclub_headers
        fanclub_headers['authorization'] = self.getAuthToken()
        
        response = self.session.put('https://www.funko.com/api/users', headers=fanclub_headers, data=data)

        if response.status_code != 200:
            print("Account fanclub signup failed")
            return False

        else:
            print("Account successfully signed up")
            return True
    
    def addAddress(self, address_json):
        new_address = address.Address(self.session, self.firstName, self.lastName, address_json)
        address_headers = headers.submit_address_header
        address_headers['authorization'] = self.getAuthToken()

        valid_address_data = new_address.getAddress()
        if valid_address_data == False:
            print("No valid address parsed")
            return False
        
        response = self.session.post('https://www.funko.com/api/address', headers=address_headers, data=valid_address_data)

        if response.status_code != 200:
            print("Account address failed to add")
            return False

        else:
            print("Account successfully added address")
            return True