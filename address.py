import requests
import geojson
from resources import form_data, headers

class Address:

    def __init__(self):
        self.data = form_data.address_data
        self.header = headers.address_verification_headers
        self.addresses = r'resources\random_address.geojson'
    
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

    def parseJson(self):
        with open(self.addresses) as file:
            gj = geojson.load(file)
        
        return gj







""" response = requests.post('https://www.funko.com/api/address/verify', headers=headers, data=data)
print(response)
print(response.text) """

new_address = Address()
new_address.formatGeoJson()
new_address.parseJson()