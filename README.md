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
