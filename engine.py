import task
import proxy
import string
import random

class Engine:

    def __init__(self):
        self.proxyList = 'resources\proxy.txt'
        self.accountList = r'resources\accounts.txt'

        self.validProxies = []
        self.validAccounts = []
        self.tasks = []

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

    def validateAccountList(self):
        accounts = self.parseTextFile(self.accountList)

        for account in accounts:
            if account.find("@") != -1: #Checks for email
                self.validAccounts.append(account)
    
    def createTasks(self):
        count = 0

        for account in self.validAccounts:
            if count >= len(self.validProxies): #reusing proxies if not enough
                count = 0
            
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            newTask = task.Task(account, password, self.validProxies[count])
            self.tasks.append(newTask)

            count += 1