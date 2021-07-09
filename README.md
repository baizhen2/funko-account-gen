# Funko.com account generator

A request-based account generator for Funko's Shopify website Funko.com

- Supports Fanclub signup
- Supports *"Random Address"* setup 
- Supports IP authentication and Username:Password Proxies 


## Windows Installation

 - Click Code > Download ZIP > Create a folder on your PC > Extract All Files to that folder

 - Open command prompt - cmd  

We are making use of pyinstaller to create a standalone .exe 

 - In cmd install pyinstaller using ```pip install pyinstaller```

 - Change directory to the folder of extracted files ex. ```cd C:\Users\Baizhen\Desktop\funko-acc-gen```

 - Then run this command ```pyinstaller --onefile main_app.py```
 
**The following step is very important** 

 - If installed correctly, a folder will be created named dist and within it, the .exe

 - You **MUST** drag the .exe file outside of the dist folder, this is so the application can correctly resolve the path of the proxies, accounts, and geojson data
 
 - The end result should look something like this. Run the application like every other application. 
![Capture](https://user-images.githubusercontent.com/62679957/125016171-dde07100-e03e-11eb-9644-da3995e94bfb.PNG)

## Proxies
The proxy.txt file in the resources folder is where you input proxies. The application will use a proxy per task and reuse proxies if there aren't enough for every task. Proxies are suggested when making multiple accounts. 

## Accounts
The accounts.txt file in the resources folder is where you input emails that you want to generate accounts for. 

## Addresses
The random_address.geojson file in the resources folder is where you input geojson data for "random" addresses.
 - Make an account at https://openaddresses.io and then navigate to https://batch.openaddresses.io/data. 
 - I highly suggest choosing a state and downloading that data because the other data collections can take up to 19gbs. 
 - The application currently only parses information from the random_address.geojson file. Do **NOT** rename the file.
 - More information can be found in the random_address.geojson file when installed.

## Engine/Task flow 
### Engine
- The application first prompts for a 2captcha key (3rd party captcha solver).
- It then parses and validates all of the proxies in proxy.txt
- The geojson is formatted to regular json.
### Task
- A request is sent to 2captcha to generate a valid captcha token for the Fanclub signup. 
- The account is generated.
- The Fanclub gets signed up.
- A random address is added to the account.
- It starts the process over again with the next email.
- A task usually is complete in 30 seconds. 

## Improvements 
Tons of improvements in terms of task speed. 

### Speed
1. **Captcha harvesting is by far the slowest process. 2captcha is slow when they are under heavy load.**
#### Potiential solutions
i. Pre-harvesting captcha tokens. However, a potential problem is tokens that aren't used in 120 seconds are no longer valid. 

ii. Harvesting tokens straight from Gmail accounts. While this may be efficient and near-instant captcha tokens for the first ~10-20 accounts, the invisible v2 captcha that the Gmail account provides will no longer be invisible and force the user to solve an image challenge to return a valid token. 

iii. Multiprocessing and threading. This can let multiple tasks run simultaneously. Haven't really looked into it but this can bring multiple improvements such as generating captcha tokens while tasks are generating new accounts. This would be the one big improvement to make this script jump from good to great.

2. **Task Flow. While the task flow is very logical, it is not very fast.**

i. While captcha tokens are being harvested, the accounts can be generated and have the address added. It can then wait for the captcha token. This goes back to multiprocessing and using threads. 

ii. Reducing the number of requests being made. After playing around with the Funko Shopify website, I believe there is a single request that can handle both the account creation and the Fanclub signup. However, I will keep that to myself for now or maybe whoever reads this can maybe find that endpoint! :wink:

## Final Thoughts 

This is my first request-based script. Before this, I mainly used libraries such as selenium to do browser automation. Browser automation is really slow compared to this and also has other pitfalls so it was time to move on. 

My favorite part of this project was reverse engineering and understanding how the website sends and received data with its requests. I now understand the overall workings of its endpoints, and potentially exploit them to make accounts even faster. I do not plan on open-sourcing that script though. :joy:

I'm going to reverse some javascript now! Thanks for reading if you made it this far! :blush:
## License
[MIT](https://choosealicense.com/licenses/mit/)
