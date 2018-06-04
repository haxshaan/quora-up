__author__ = "Shantam Mathuria"
__copyright__ = "Copyright 2018, The Cogent Project"
__credits__ = ["Shantam Mathuria"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Shantam Mathuria"
__email__ = "shantam.m22@gmail.com"
__status__ = "Production"

import time
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Reading the configuration file
par = ConfigParser()
par.read('config.ini')
parameters = {}

# Dictionary for storing the parsed parameters
for section_name in par.sections():
        # Parsing the configuration file and reading it into the dict
        for name, value in par.items(section_name):
                parameters[name] = value
                
# Automating your browser 
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.quora.com")
time.sleep(3)
