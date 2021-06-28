import task
import proxy

class Engine:

    def __init__(self):
        self.proxyList = 'resources\proxy.txt'
        self.accountList = r'resources\accounts.txt'

        self.validProxies = []

    def parseTextFile(self, file):
        f = open(file)

        parsed = []
        for x in f:
            parsed.append(x.rstrip('\n'))
        
        return parsed
    
    def validateProxyList(self):
        proxies = self.parseTextFile(self.proxyList)

        for index in proxies:
            new_proxy = proxy.Proxy(index)
            if new_proxy.validateProxy() != None:
                self.validProxies.append(new_proxy.proxyFormat)

    
        



