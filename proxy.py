import requests

class Proxy:

    def __init__(self, proxy):
        self.proxy = proxy.split(":")

        self.proxyFormat = {
            'https': ""
        }

        self.session = requests.Session()

        self.proxyAlive = False
        
    def parseProxy(self):
        if len(self.proxy) == 2: #ip:port
            self.proxyFormat['https'] = 'http://' + self.proxy[0] + ":" + self.proxy[1]
        
        elif len(self.proxy) == 4: #ip:port:username:password
            self.proxyFormat['https'] = 'http://' + self.proxy[2] + ":" + self.proxy[3] + "@" + self.proxy[0] + ":" + self.proxy[1]
        
        else:
            self.proxyFormat['https'] = None

    def isProxyWorking(self):
        
        #handles bad proxy format
        if self.proxyFormat['https'] != None:
            self.session.proxies.update(self.proxyFormat)
        else:
            return None

        #handles proxy connection issues
        try:
            response = self.session.get("https://httpbin.org/ip")

            if response.status_code == 200:
                self.proxyAlive = True

        except requests.exceptions.RequestException:
            print("Proxy error")
            
        else:
            print("Unknown Error")
    
    def validateProxy(self):
        self.parseProxy()
        self.isProxyWorking()

        if self.proxyAlive == True:
            return self.proxyFormat
        
        return None