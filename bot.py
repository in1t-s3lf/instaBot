import os
import time
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

creds = []
usern0 = []
usern1 = []
proxies = []
message_ = input("Type your message here: ")
urll = 'https://www.instagram.com/'

ll = logging.basicConfig(filename='instabot.log', 
            format='%(asctime)s %(message)s', 
            filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def getinfo():
    with open('user_list_0') as un:
        for nme in un:
            usern0.append(nme.strip('\n'))

    with open('proxies') as pro:
        for p in pro:
            proxies.append(p.strip('\n'))

    with open('allnmes') as foo:
        for bar in foo:
            creds.append(bar.strip('\n'))
'''
    with open('user_list_1') as prr:
        for pr in prr:
            usern1.append(pr.strip('\n'))
'''
class bot:

    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message =  message
        self.base_url = urll
        self.bot = webdriver.Firefox()
        self.login()

    def login(self):
        while True:
            try:
                self.bot.get(self.base_url)
                enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
                enter_username.send_keys(self.username)
                enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
                enter_password.send_keys(self.password)
                enter_password.send_keys(Keys.RETURN)
                time.sleep(5)
                self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
                time.sleep(3)
                self.bot.find_element_by_class_name('xWeGp').click()
                time.sleep(4)
                self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
                time.sleep(3)
                self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
                msg = WebDriverWait(self.bot, 3).until(expected_conditions.presence_of_element_located((By.NAME, 'queryBox')))
                msg.send_keys(self.user)
                time.sleep(3)
                self.bot.find_element_by_xpath('//button[@class="dCJp8 "]').click()
                time.sleep(2)
                self.bot.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF   cB_4K  "]').click()
                time.sleep(4)
                self.bot.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(self.message)
                time.sleep(3)
                self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                self.bot.close()
                logger.debug("The code is working fine.")
        
            except NoSuchElementException:
                logger.error("Element not found.")
                print('Element not found')
                continue

            except TimeoutException:
                logger.critical('Loading is taking long')
                print('Loading took too much time.')
                continue
            break


def init():     
    '''
    for u0 in usern0:
        bot(0,creds[0].split(':')[0], creds[0].split(':')[1], u0, message_)
        print('[+] message sent to:' + u)
    '''
    for u1 in usern0:
        bot( creds[1].split(':')[0], creds[1].split(':')[1], u1, message_)
        print('[+] message sent to:' + u1)
        time.sleep(480)

getinfo()
init()

