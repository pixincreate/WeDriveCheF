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

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


# Provides the facility to run on both terminal as well as in the python console
def resource_path(another_way):
    try:
        usual_way = sys._MEIPASS
    except AttributeError:
        usual_way = os.path.dirname(__file__)
    return os.path.join(usual_way, another_way)


def web_driver():
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
    if 'Brave-Browser' == flag or 'Brave-Browser-Nightly' == flag:
        options.binary_location = f"C:\\Program Files\\BraveSoftware\\{flag}\\Application\\brave.exe"
        is_chromium = True
    elif 'Firefox' == flag:
        options = FirefoxOptions()
        is_chromium = False
    elif 'Chrome' == flag:
        print("Google Chrome is NOT RECOMMENDED due to it's stance on user privacy.\n"
              "PiX recommends you using Firefox or Brave instead.\n"
              "Also, as per the reports, Chrome is the most insecure browser to be existent!")
        is_chromium = True
    elif 'Edge' == flag:
        print("Edge is unsupported because PiX don't use it!")
    else:
        print("No browser is supported on your PC."
              "Kindly install 'Brave' or 'Firefox' to get this module working!")

    # options.add_argument("--headless")
    try:
        if is_chromium:
            options.add_argument("--incognito")
            driver = webdriver.Chrome(service=Service(executable_path=resource_path('web_drivers\\chromedriver.exe')),
                                      options=options)
        else:
            options.add_argument("--private")
            driver = webdriver.Firefox(service=FirefoxService(
                executable_path=resource_path('web_drivers\\geckodriver.exe')),
                options=options)
    except FileNotFoundError:
        print("Webdriver seems to be outdated, try updating the webdriver..", end='\n')

    return driver
