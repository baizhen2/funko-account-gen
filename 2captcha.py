from twocaptcha import TwoCaptcha

class Solver:

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.siteKey = '6LfNWXEUAAAAAMADpc9mxhXTP-XNunQNrs7GDMHi'
        self.site = 'https://www.funko.com/'

    def solve(self):
        solver = TwoCaptcha(self.apiKey)
        captcha = solver.recaptcha(sitekey=self.siteKey, url=self.site)
        token = captcha['code']
        return token

solver = Solver("4f4498353c433e69b3353be8a2fdf888")
captcha = solver.solve()
print(captcha)
