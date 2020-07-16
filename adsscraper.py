import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from pymongo import MongoClient
import sys
from selenium.webdriver.common.keys import Keys

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

def scrollToBotton():
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(randint(3,6))
        ht = driver.execute_script("""window.scrollTo(0, document.body.scrollHeight); return window.scrollHeight;""")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0)")

def clickAllAds():
    ads_text_div = driver.find_elements_by_xpath('//div[starts-with(@class,"_7jyr")]')
    time.sleep(3)
    for ad in ads_text_div:
        ad.click()
        time.sleep(randint(3,6))
    


driver = webdriver.Chrome(ChromeDriverManager().install())

loadAds()
scrollToBotton()
clickAllAds()

driver.close()
