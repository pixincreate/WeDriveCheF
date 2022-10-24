#
# Creative Commons Legal Code
#
# CC0 1.0 Universal
#
#     Copyright © pixincreate
#
#     CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
#     LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
#     ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
#     INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
#     REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
#     PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
#     THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
#     HEREUNDER.
#
#

import os
import sys

import winapps
import traceback
import webbrowser

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.common.exceptions import WebDriverException


# Provides the facility to run on both terminal as well as in the python console
def resource_path(another_way):
    try:
        usual_way = sys._MEIPASS
    except AttributeError:
        usual_way = os.path.dirname(__file__)
    return os.path.join(usual_way, another_way)


def error():
    print("Webdriver seems to be outdated, try updating the webdriver in correspondence to your browser version..",
          end='\n')
    webbrowser.open('https://chromedriver.chromium.org/downloads', new=2)


# Functionality
def web_driver(head_mode):
    # Fetches the application list from your installed apps
    for item in winapps.list_installed():
        item = item.name
        if 'Brave Nightly' in item:
            flag = 'Brave-Browser-Nightly'
        elif 'Brave' in item:
            flag = 'Brave-Browser'
        if 'Chrome' in item:
            flag = 'Chrome'
        elif 'Firefox' in item:
            flag = 'Firefox'

    options = Options()
    # Checks for Chromium based browser i.e., Brave
    if 'Brave-Browser' == flag or 'Brave-Browser-Nightly' == flag:
        options.binary_location = f"C:\\Program Files\\BraveSoftware\\{flag}\\Application\\brave.exe"
        is_chromium = True

    # Checks for the existence of Firefox
    elif 'Firefox' == flag:
        options = FirefoxOptions()

    # Checks whether the browser selected is Google Chrome which I do not recommend using it whatsoever
    elif 'Chrome' == flag:
        print("Google Chrome is NOT RECOMMENDED due to it's stance on user privacy.\n"
              "PiX recommends you using Firefox or Brave instead.\n"
              "Also, as per the reports, Chrome is the most insecure browser to be existent!")
        is_chromium = True

    # Edge is unsupported as I want to take revenge against Microsoft, LOL
    elif 'Edge' == flag:
        print("Edge is unsupported because PiX don't use it!")

    # Rare condition!
    else:
        print("No browser is supported on your PC."
              "Kindly install 'Brave' or 'Firefox' to get this module working!")

    if head_mode == 'headless':
        options.add_argument(f"--{head_mode}")

    try:
        # If the webdriver is up to-date
        # and it is chromium (blink) based browser
        if is_chromium:
            options.add_argument("--incognito")
            try:
                driver = webdriver.Chrome(
                    service=Service(executable_path=resource_path('web_drivers\\chromedriver.exe')),
                    options=options)
            # If the Webdriver is outdated or it doesn't exist!
            except FileNotFoundError:
                error()
            except WebDriverException:
                error()
        # if the browser is based on Firefox
        else:
            options.add_argument("--private")
            try:
                driver = webdriver.Firefox(service=FirefoxService(
                    executable_path=resource_path('web_drivers\\geckodriver.exe')),
                    options=options)
            # If the Webdriver is outdated or it doesn't exist!
            except FileNotFoundError:
                error()
            except WebDriverException:
                error()
    except Exception as e:
        driver.quit()
        print('Error: ', e)
        traceback.print_exc()
    try:
        return driver
    except UnboundLocalError:
        quit()


web = web_driver('lol')
web.get('https://pixincreate.github.io')
web.quit()