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
    search_bar.send_keys("Iman Gadzhi")
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
    ads_copy_div = driver.find_elements_by_xpath('//div[@class="_7jyr"]')
    time.sleep(3)
    for ad in ads_copy_div:
        try:
            ad.click()
            time.sleep(1.5)
        except:
            ads_copy_div.remove(ad)
    driver.execute_script("window.scrollTo(0, 0)")
    return ads_copy_div


# def peristAds():
    # started_running = driver.find_elements_by_xpath('//div[@class="_7jwu"]')
    # #platforms = driver.find_element_by_xpath('//div[starts-with(@class,"_3qn7")]').find_element_by_xpath('//i').get_attribute("class")
    # platforms = driver.find_elements_by_xpath('//div[@class="_8k-_"]')
    # #print('Facebook' if platform == 'img sp_qqiEEYnS8_M sx_b88b1a' else 'Other platform')
    # ads_copy_div = driver.find_elements_by_xpath('//div[@class="_7jyr"]')
    # headlines = driver.find_elements_by_xpath('//div[@class="_8jh2"]')
    # #driver.find_element_by_xpath('//a[starts-with(@class,"_231w")]').get_property('href')
    # #driver.find_element_by_xpath('//img[starts-with(@class,"_7jys")]').get_property('src')
    # urls = driver.find_elements_by_xpath('//img[starts-with(@class,"_7jys")]')

    # creative_urls = driver.find_element_by_xpath('//img[starts-with(@class,"_7jys")]').get_property('src')
    # # creative_url = driver.find_element_by_xpath('//img[starts-with(@class,"_7jys")]').get_property('src')
    # # counter = 1
    # # file_creative_name = "SamOvens_creative" + str(counter)
    # # r = requests.get(creative_url, stream = True)
    # # r.raw.decode_content = True
    # # print(file_creative_name)
    # count = 0
    # newArrayOfCopy = []
    # for copy in ads_copy_div:
        # if (copy.is_displayed() == True): 
            # newArrayOfCopy.append(copy)

    # print("Started runnign date: " + str(len(started_running)))
    # print("Platforms: " + str(len(platforms)))
    # print("Ads Copy: " + str(len(newArrayOfCopy)))
    # print("Headlines: " + str(len(headlines)))
    # print("URLS: " + str(len(urls)))
    # print("Creative urls: " + str(len(creative_urls)))
    # printArrayText(newArrayOfCopy)

def peristAds():
    ad_containers = driver.find_elements_by_xpath('//div[@class="_99s5"]')
    displayed_containers = []
    for ad in ad_containers:
        if (ad.is_displayed() == True): 
            displayed_containers.append(ad)
    print(len(displayed_containers))
    ad_container_1 = ad_containers[1]
    started_running = ad_container_1.find_element_by_xpath('//div[@class="_7jwu"]')
    print(started_running.text)
    platform = ad_container_1.find_element_by_xpath('.//div[starts-with(@class,"_3qn7")]').find_element_by_xpath('//i').get_attribute("class")
    print('Facebook' if platform == 'img sp_qqiEEYnS8_M sx_b88b1a' else 'Other platform')
    print(ad_container_1.find_element_by_xpath('.//div[@class="_7jyr"]').text)
    print(ad_container_1.find_element_by_xpath('.//div[@class="_8jh2"]').text)
    print(ad_container_1.find_element_by_xpath('.//a[starts-with(@class,"_231w")]').get_attribute('href'))
    print(ad_container_1.find_element_by_xpath('.//img[starts-with(@class,"_7jys")]').get_property('src'))

    creative_url = ad_container_1.find_element_by_xpath('.//img[starts-with(@class,"_7jys")]').get_property('src')



driver = webdriver.Chrome(ChromeDriverManager().install())

loadAds()
scrollToBotton()
ads = clickAllAds()
peristAds()

driver.close()
