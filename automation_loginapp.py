"""This program is script for atomation of login on my bank application"""

import argparse
from selenium import webdriver

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()

driver = webdriver.Chrome()
driver.get("http://localhost:8000/customer/")

username = driver.find_element_by_xpath("/html/body/form/div/input[1]")
username.send_keys(args.username)
password = driver.find_element_by_xpath("/html/body/form/div/input[2]")
password.send_keys(args.password)

login = driver.find_element_by_xpath("/html/body/form/div/button")
login.click()
