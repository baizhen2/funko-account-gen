import requests
import names
from resources import headers, form_data

class Task:

    def __init__(self, email, password, proxy):
        self.email = email
        self.password = password #password created from task engine
        self.proxy = proxy #proxyDict formatted from task engine

        self.session = requests.Session()

    def proxySetup(self):
        self.session.proxies.update(self.proxy)

    def formSetup(self):
        return form_data.fillAccForm(
            names.get_first_name(),
            names.get_last_name(),
            self.email,
            self.password
        )

    def generateAccount(self):
        self.proxySetup()
        data = self.formSetup()

        response = requests.post('https://www.funko.com/api/users/signup', headers=headers.create_acc_headers, data=data)

        if response.status_code != 200:
            print("Account creation failed")
            return False

        else:
            print("Account created")
            return True