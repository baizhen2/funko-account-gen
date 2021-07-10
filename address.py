import requests
import json
import random
import time
from resources import form_data, headers

class Address:

    def __init__(self, session, firstName, lastName, address_json):
        self.data = form_data.address_data
        self.header = headers.address_verification_headers
        
        self.json_obj = address_json
        self.address_data = None

        self.session = session
        self.firstName = firstName
        self.lastName = lastName

    def formatAddress(self):
        random_num = random.randint(0, len(self.json_obj) - 1)

        address = self.json_obj[random_num]
        city = address["properties"]["city"]
        line_one = address["properties"]["number"] + " " + address["properties"]["street"]
        state = address["properties"]["region"]
        zipcode = address["properties"]["postcode"]

        if zipcode == "":
            zipcode = self.getZipcode()

        self.address_data = form_data.fillAddressInfo(self.firstName, self.lastName, line_one, city, state, zipcode)
        print(self.address_data)

    def verifyAddress(self):
        response = self.session.post('https://www.funko.com/api/address/verify', headers=self.header, data=self.address_data)

        data = json.loads(response.text)
        print("Response: " + str(data))
                
        try:
            if data[0]["exactMatch"] == False:
                line_one = data["candidates"][0]["addressLine"][0]
                city = data["candidates"][0]["city"]
                state = data["candidates"][0]["state"]
                zipcode = data["candidates"][0]["postalCode"]
                self.address_data = form_data.fillAddressInfo(self.firstName, self.lastName, line_one, city, state, zipcode)
                print(self.address_data)

                return True #Returns true because there is a valid address candidate
            
            if data[0]["exactMatch"] == True:
                return True

        except KeyError: #Bad request to funko servers returning {'candidates': []}
            print("keyError")
            return False

        return False
    
    def getAddress(self):
        verification = False
        retries = 0

        while verification == False:
            time.sleep(2)
            self.formatAddress()
            verification = self.verifyAddress()
            print("verification is: ")
            print(verification)
            
            if retries == 3:
                return False
                
            retries += 1
        
        return self.address_data

    def getZipcode(self):
        return random.randint(15000, 90000)