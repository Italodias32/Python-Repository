from selenium import webdriver
import time

chrome = webdriver.Chrome()
chrome.get('https://afazenda.r7.com/a-fazenda-12')
chrome.maximize_window() 
chrome.implicitly_wait(3000)

clica = chrome.find_element_by_xpath('//*[@id="box_5f629c8dca9084ecee000a1a"]/div/div/div/div/section/div[2]/figure[2]/button')
clica.click()
count = 1

while count != 10000000:
    clica = chrome.find_element_by_xpath('//*[@id="755"]')
    clica.click()
    clica = chrome.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/div[1]/div[1]/button')
    clica.click()
    clica = chrome.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/div[1]/div/div[1]/div/div/button')
    clica.click()
    print(count)
    count = count + 1