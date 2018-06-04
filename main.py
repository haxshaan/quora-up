__author__ = "Shantam Mathuria"
__copyright__ = "Don't steal bitches"
__credits__ = ["Shantam Mathuria"]
__license__ = "None of your business"
__version__ = "1.0.1"
__maintainer__ = "Ofc Me"
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

# Filling the login credentials
form = driver.find_element_by_class_name('regular_login')
email = form.find_element_by_name("email")
email.send_keys(parameters["email_id"])
password = form.find_element_by_name("password")
password.send_keys(parameters["pass_word"])
password.send_keys(Keys.RETURN)
time.sleep(3)       

# Getting to other user's link ;) 
answers_link = "https://www.quora.com/" + parameters["user_name"]
driver.get(answers_link)                                                        
time.sleep(2)

# Let's retrieve the whole page so that you don't miss a single answer
while 1:
        a = driver.execute_script("return document.body.scrollHeight;")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        b = driver.execute_script("return document.body.scrollHeight;")
        if a==b:
                break
                
# Time to upvote the answers ;)                                  
driver.execute_script("window.a = document.getElementsByClassName('icon_action_bar-button blue_icon');")

# Retrieving all the upvote items in an array
driver.execute_script("for(var i=0; i<a.length; i++) { a[i].click(); }")

# Clicking on each and every item one by one
print('All answers upvoted :D\n')
                
