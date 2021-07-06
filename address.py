import requests
import json
import random
from resources import form_data, headers

class Address:

    def __init__(self, session, firstName, lastName, address_json):
        self.data = form_data.address_data
        self.header = headers.address_verification_headers
        self.addresses = r'resources\random_address.geojson'
        
        self.json_obj = address_json
        self.address_data = None

        self.session = session
        self.firstName = firstName
        self.lastName = lastName

    def formatGeoJson(self):
        with open(self.addresses) as file:
            lines = file.read().splitlines()
        
        with open(self.addresses, "w") as file:
            line_count = 0
            last_line = len(lines) - 1

            for line in lines:
                if line_count == 0:
                    file.write("[" + line + ",\n")
                if line_count == last_line:
                    file.write(line + "]")
                else:
                    file.write(line + ",\n")
                line_count += 1

        with open(self.addresses) as file:
            gj = geojson.load(file)
        
        self.json_obj = gj

    def formatAddress(self):
        random_num = random.randint(0, len(self.json_obj) - 1)

        address = self.json_obj[random_num]
        city = address["properties"]["city"]
        line_one = address["properties"]["number"] + " " + address["properties"]["street"]
        state = address["properties"]["region"]
        zipcode = address["properties"]["postcode"]

        self.address_data = form_data.fillAddressInfo(self.firstName, self.lastName, line_one, city, state, zipcode)

    def verifyAddress(self):
        response = self.session.post('https://www.funko.com/api/address/verify', headers=self.header, data=self.address_data)

        data = json.loads(response.text)
                
        try:
            if data["exactMatch"] == False:
                line_one = data["candidates"][0]["addressLine"]
                city = data["candidates"][0]["city"]
                state = data["candidates"][0]["state"]
                zipcode = data["candidates"][0]["postalCode"]
                self.address_data = form_data.fillAddressInfo(self.firstName, self.lastName, line_one, city, state, zipcode)
            
            if data["exactMatch"] == True:
                return True

        except KeyError: #Bad request to funko servers returning {'candidates': []}
            return False

        return False