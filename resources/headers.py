create_acc_headers = {
    'authority': 'www.funko.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.funko.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.funko.com/register',
    'accept-language': 'en-US,en;q=0.9',
}

import requests

headers = {
    'authority': 'www.funko.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.funko.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.funko.com/my-account',
    'accept-language': 'en-US,en;q=0.9',
}

data = '{"email":"bobfline@beebuxaio.com","fanClubOptOut":false,"birthMonth":"4","birthDay":"17","captcharesponse":"03AGdBq24-sVAxg9f99mr7_5DHj24j4AKolRjaItdDbPUW3HoscTYM9CoViyEJJv5X-AHtjY_SxqoPS_Glktzi8h4J-5q9-_zJnRhDmxnmOeD09MQkPsh2t0W8I_V_4PmxwVaekH7XqsOXAi9_xSVzY_JAFnpWbY8T8Fp_lADikaxAIrBgechtjNhuOYBOClmAO7aPHX_-0r0PjNlfik13TwWfTkkzvTtMefqssyKqGXi1Rkal9tDWVO9e4UEECXVcI04jj_G6jfS_oEk--OVJp7vqs49vkPLIFO9j55Bz4MxRj8IsGiUCYMFEPb4wCtV560ua0JnwW4ByMe4uSAVu0LIAQlePwKKvYxZreTTinfvJQMZsq_lVhKA-AOMfZniexhTNvrYrVUusYziLDYl6S-h-xKvOvfsJgFF6h0rInZ0-vZD37RUVvL02VzgYXiztuOtp6AaItGNx"}'

response = requests.put('https://www.funko.com/api/users', headers=headers, data=data)
