import time
from datetime import date
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from pymongo import MongoClient
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
import requests
import os

class ad():
    pass

def loadAds():
    driver.get("https://www.facebook.com/ads/library/")
    time.sleep(4)
    search_bar = driver.find_element_by_xpath('//input[starts-with(@type,"text")]')
    time.sleep(1)
    search_bar.send_keys(fb_page)
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
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0)")
    return ads_copy_div

def peristAds():
    ad_containers = driver.find_elements_by_xpath('//div[@class="_99s5"]')
    displayed_containers = cleanContainer(ad_containers) 
    database_name = fb_page.replace(' ', '_')
    client = MongoClient()
    db = client['ads']
    collection = db[database_name]
    for i, ad in enumerate(displayed_containers):
        collection.insert_one(createSingleAd(ad, i))
    client.close()

def cleanContainer(ad_containers):
    return [ad for ad in ad_containers if ad.is_displayed()]

def createSingleAd(ad, counter):
    started_running = ad.find_element_by_xpath('.//div[@class="_7jwu"]').text
    copy = ad.find_element_by_xpath('.//div[@class="_7jyr"]').text
    headline = ad.find_element_by_xpath('.//div[@class="_8jh2"]').text
    fb_destination_link = "No link"
    try:
        fb_destination_link = parseLink(ad.find_element_by_xpath('.//a[starts-with(@class,"_231w")]').get_attribute('href'))
    except:
        pass
    image_facebook_link = None 
    video = False
    try:
        image_facebook_link = ad.find_element_by_xpath('.//img[starts-with(@class,"_7jys")]').get_property('src')
    except:
        video = True
        image_facebook_link = ad.find_element_by_xpath('.//video').get_property('poster')
    file_creative_name = fb_page + "_creative" + str(counter)
    file_path = os.path.abspath(os.getcwd()) + '/' +  file_creative_name
    file_path_destination = os.path.abspath(os.getcwd()) + '/images/'
    r = requests.get(image_facebook_link, stream = True)
    r.raw.decode_content = True
    with open(file_creative_name, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
        shutil.move(file_path, file_path_destination)
    an_ad = {}
    an_ad['niche'] = niche 
    an_ad['products'] = products 
    an_ad['date_retrieved'] = today 
    an_ad['started_running'] = started_running
    an_ad['copy'] = copy
    an_ad['headline'] = headline
    an_ad['fb_destination_link'] = fb_destination_link
    an_ad['image_facebook_link'] = image_facebook_link
    if video:
        an_ad['video'] = "True" 
    an_ad['fb_destination_link'] = fb_destination_link
    return an_ad

def parseLink(link):
    if '=http' in link:
        slicer = slice(link.index('=http') + 1, link.index('h=') - 1)
        link = link[slicer].replace('%2F', '/').replace('%3A', ':').replace('%3F', '?').replace('%3D', '=')
    return link

driver = webdriver.Chrome(ChromeDriverManager().install())
today = date.today().strftime('%d/%m/%Y')
fb_page = str(sys.argv[1])
niche = str(sys.argv[2])
products = str(sys.argv[3])
loadAds()
scrollToBotton()
clickAllAds()
peristAds()

driver.close()
