import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from pymongo import MongoClient
from bson.binary import Binary
import sys, os
from selenium.webdriver.common.keys import Keys
import requests
import shutil

class ad():
    pass

def loadAds():
    driver.get("https://www.facebook.com/ads/library/")
    time.sleep(4)
    search_bar = driver.find_element_by_xpath('//input[starts-with(@type,"text")]')
    time.sleep(1)
    search_bar.send_keys("Sam Ovens")
    time.sleep(3)

    driver.find_element_by_xpath('//div[starts-with(@class,"_7h2l")]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//button[starts-with(@type,"button")]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//li[starts-with(@data-testid,"all-ad-type-tab")]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//span[starts-with(@class,"_7fc8")]').click()
    time.sleep(3)

    driver.find_element_by_xpath('//div[starts-with(@class,"ellipsis")]').click()
    time.sleep(3)


    search_bar = driver.find_element_by_xpath('//input[starts-with(@type,"text")]')
    search_bar.click()
    time.sleep(2)

    driver.find_element_by_xpath('//div[starts-with(@class,"_7h2l")]').click()
    time.sleep(3)


def clickOneAd():
    ad = driver.find_element_by_xpath('//div[@class="_7jyr"]')
    time.sleep(3)
    ad.click()
    time.sleep(randint(3,6))

def peristAds():
    ad = driver.find_element_by_xpath('//div[@class="_7jyr"]')
    print(driver.find_element_by_xpath('//div[@class="_7jwu"]').text)
    platform = driver.find_element_by_xpath('//div[starts-with(@class,"_3qn7")]').find_element_by_xpath('//i').get_attribute("class")
    print('Facebook' if platform == 'img sp_qqiEEYnS8_M sx_b88b1a' else 'Other platform')
    print(driver.find_element_by_xpath('//div[@class="_7jyr"]').text)
    print(driver.find_element_by_xpath('//div[@class="_8jh2"]').text)
    print(driver.find_element_by_xpath('//a[starts-with(@class,"_231w")]').get_property('href'))
    print(driver.find_element_by_xpath('//img[starts-with(@class,"_7jys")]').get_property('src'))

    creative_url = driver.find_element_by_xpath('//img[starts-with(@class,"_7jys")]').get_property('src')
    counter = 1
    file_creative_name = "SamOvens_creative" + str(counter)
    file_path = os.path.abspath(os.getcwd()) + '/' +  file_creative_name
    file_path_destination = os.path.abspath(os.getcwd()) + '/images/'
    print(file_path)
    r = requests.get(creative_url, stream = True)
    r.raw.decode_content = True
    with open(file_creative_name, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
        shutil.move(file_path, file_path_destination)



driver = webdriver.Chrome(ChromeDriverManager().install())

loadAds()
clickOneAd()
peristAds()

driver.close()
