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
from sys import exit


# Reading the configuration file
par = ConfigParser()
par.read('config.ini')
parameters = {}

ulist = dict()

with open("accounts.ini", 'r') as f:
    doc = f.read().split('\n')
    num_ac = 0
    for item in doc:
        if not (
                ' ' or '.' or
                '@'
        ) in item:
            print("Check account: ", item)
            exit(0)
        else:
            ulist.update({(item.split()[0]): (item.split()[1])})
            num_ac += 1


def main(u, p):

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
    email.send_keys(u)
    password = form.find_element_by_name("password")
    password.send_keys(p)
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
            if a == b:
                break

    # Time to upvote the answers ;)
    driver.execute_script("window.a = document.getElementsByClassName('icon_action_bar-button blue_icon');")

    # Retrieving all the upvote items in an array
    driver.execute_script("for(var i=0; i<a.length; i++) { a[i].click(); }")

    # Clicking on each and every item one by one
    print('All answers upvoted :D\n')
    driver.implicitly_wait(6)
    driver.quit()


if __name__ == '__main__':

    print("Welcome to Hax Quoara Upvoter!\n")

    print("Parsing account file in the buffer\n")

    print("Total accounts found: ", num_ac)

    for uname, passw in ulist.items():
        main(uname, passw)
