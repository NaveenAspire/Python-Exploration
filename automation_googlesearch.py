"""This module code for send the serach things using argparser and
 serach result will show in Google"""
import argparse
from selenium import webdriver

parser = argparse.ArgumentParser()
parser.add_argument("--search", default="Aspire Systems")
args = parser.parse_args()

driver = webdriver.Chrome()
driver.get("https://www.Google.com/")

search = driver.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input"
)
search.send_keys(args.search)

search.submit()
