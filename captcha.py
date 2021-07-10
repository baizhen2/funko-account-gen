from twocaptcha import TwoCaptcha

class Solver:

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.siteKey = '6LfNWXEUAAAAAMADpc9mxhXTP-XNunQNrs7GDMHi'
        self.site = 'https://www.funko.com/'

    def solve(self):
        print("Getting captcha token")
        solver = TwoCaptcha(self.apiKey)
        captcha = solver.recaptcha(sitekey=self.siteKey, url=self.site)
        token = captcha['code']
        print(token)
        return token