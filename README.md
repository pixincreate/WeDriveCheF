# Driver Checker and Fetcher (Suggest a better name, thanks!)

As the title says, this tiny module's only job is to check for suitable `web_driver` on your PC for ease of use.  

Based on CC0 1.0 Universal License.  

## Usage:
```commandline
# Enter your URL here or directly inside the `get` function
URL = "https://pixincreate.github.io"

# Call the webdriver on your code by typing the below command
# This assigns the suitable driver found on your PC

# head_mode may be `head` or `headless`
driver = web_driver(head_mode)

# Web driver opens up the link with desired head_mode. 
driver.get(URL)
```
