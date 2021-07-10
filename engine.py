import task
import proxy
import string
import random
import captcha
import time
import geojson

class Engine:

    def __init__(self):
        self.proxyList = r'resources/proxy.txt'
        self.accountList = r'resources/accounts.txt'
        self.addresses = r'resources/random_address.geojson'
        self.solver = None
        self.address_json = None

        self.validProxies = []
        self.validAccounts = []
        self.tasks = []

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
        
        self.address_json = gj

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
    
    def setupSolver(self):
        apiKey = input("Enter 2captcha api key: ")
        self.solver = captcha.Solver(apiKey)

    def createTasks(self):
        count = 0

        for account in self.validAccounts:
            if count >= len(self.validProxies): #reusing proxies if not enough
                count = 0
            
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            newTask = task.Task(account, password, self.validProxies[count])
            self.tasks.append(newTask)

            count += 1

    def setupEngine(self):
        self.setupSolver()
        self.validateProxyList()
        self.validateAccountList()
        self.createTasks()
        self.formatGeoJson()

    def runTasks(self):
        self.setupEngine()

        file = open("generated.txt", "w+")

        for tasks in self.tasks:
            captchaToken = self.solver.solve()
            create = tasks.generateAccount()

            if create == False: #When account creation fails
                continue

            time.sleep(3)
            signup = tasks.signupFanclub(captchaToken)
            time.sleep(3)
            add_address = tasks.addAddress(self.address_json)

            if create == True and signup == True and add_address == True:
                file.write(tasks.email + ":" + tasks.password + "\n")

            if create == True and signup == True and add_address == False:
                file.write(tasks.email + ":" + tasks.password + "No Address" + "\n")
        
        file.close()