# Web Driver Checker and Fetcher [WeDriCheF]
### (Suggest a better name, thanks!)

As the title says, this tiny module's only job is to check for suitable `web_driver` on your PC for ease of use.

## Usage:
- Before using make sure you run the `requirements.txt` by using the command:  
`pip install -r requirements.txt`
```python
# Enter your URL here or directly inside the `get` function
URL = "https://pixincreate.github.io"

# Call the webdriver on your code by typing the below command
# This assigns the suitable driver found on your PC

# Put head_mode as `headless` if you want it to be headless,
# Else, give it any random value within quotes.
driver = web_driver(head_mode)

# Web driver opens up the link with desired head_mode in incognito / private mode. 
driver.get(URL)

# Make sure you use the below command once you're done with your work, else
# it'll remain active in the background drain battery and memory
driver.quit()
```
## Working:
- When you call the function `web_driver` and assign it to a `driver`, it initially goes through all your installed applications
  - No need to worry, none of your data is transmitted
- It checks for these below given browsers:
  - Brave 
  - Brave Nightly
  - Firefox
  - Google Chrome (I don't recommend using it as it is found to be insecure based on numerous reports and it is a threat to user-privacy)
-  If the browser is Brave, it assigns its binary file, if chrome or firefox, raises a flag as they're natively supported by `selenium`
- Depending on the browser type, the `driver` is assigned with `incognito/private` as the argument
  - In case, the driver doesn't exist or outdated, it automatically opens up the default web browsers to download the latest `web_driver.exe` file (you've to download this manually!)
- This `driver` is then returned to the `calling function / method` which later calls for the URL.

## Requirements:
- Operating System: Windows _(Tested only on Windows)_
- Python Version: `3.5+` (`3.10+` preferred)
- Packages Required: WinApps, Selenium (Get's installed upon running `requirements.txt`)

## LICENSE:
This repo come under _CC0 1.0 Universal_ copyrighted to `pixincreate`. Click [_here_]() to learn more about the permissions offered by this license!

