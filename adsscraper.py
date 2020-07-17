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
    ads_copy_div = driver.find_elements_by_xpath('//div[@class="_7jyr"]')
    time.sleep(3)
    for ad in ads_copy_div:
        try:
            ad.click()
            time.sleep(0.5)
        except:
            ads_copy_div.remove(ad)
    driver.execute_script("window.scrollTo(0, 0)")
    return ads_copy_div


def peristAds():
    ad_containers = driver.find_elements_by_xpath('//div[@class="_99s5"]')
    displayed_containers = cleanContainer(ad_containers) 
    # creative_url = driver.find_element_by_xpath('//img[starts-with(@class,"_7jys")]').get_property('src')
    # counter = 1
    # file_creative_name = "SamOvens_creative" + str(counter)
    # r = requests.get(creative_url, stream = True)
    # r.raw.decode_content = True
    # print(file_creative_name)

    for ad in displayed_containers:
        persistSingleAd(ad)

def cleanContainer(ad_containers):
    displayed_containers = []
    for ad in ad_containers:
        if (ad.is_displayed() == True): 
            displayed_containers.append(ad)
    return displayed_containers

def persistSingleAd(ad):
    started_running = ad.find_element_by_xpath('.//div[@class="_7jwu"]').text
    copy = ad.find_element_by_xpath('.//div[@class="_7jyr"]').text
    headline = ad.find_element_by_xpath('.//div[@class="_8jh2"]').text
    fb_destination_link = parseLink(ad.find_element_by_xpath('.//a[starts-with(@class,"_231w")]').get_attribute('href'))
    image_facebook_link = None 
    try:
        image_facebook_link = ad.find_element_by_xpath('.//img[starts-with(@class,"_7jys")]').get_property('src')
    except:
        video = True

def parseLink(link):
    first_index = link.index('=http') + 1
    second_index = link.index('h=') - 1
    slicer = slice(first_index, second_index)
    parsed_link = link[slicer].replace('%2F', '/').replace('%3A', ':').replace('%3F', '?').replace('%3D', '=')
    return parsed_link

driver = webdriver.Chrome(ChromeDriverManager().install())

loadAds()
scrollToBotton()
ads = clickAllAds()
peristAds()

driver.close()
