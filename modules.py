import time as t
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import cv2
import pytesseract
def loader():
    pytesseract.pytesseract.tesseract_cmd = r'tesseract\tesseract.exe'

def register(driver):
    t.sleep(5)
    ActionChains(driver)\
        .send_keys(Keys.ENTER)\
        .perform()
    t.sleep(1)
    driver.get_screenshot_as_file("imagescrape/Starbreak.png") 
    img = cv2.imread('imagescrape/Starbreak.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    cv2.imshow("result", img)
    t.sleep(10)
    for i in range(10):
        ActionChains(driver)\
            .send_keys("[")\
            .perform()
        ActionChains(driver)\
            .send_keys("m")\
            .send_keys("n")\
            .perform()
        ActionChains(driver)\
            .send_keys("H")\
            .perform()
    print('a')
def fillSC(driver):
    global action_key_down_RIGHT, action_key_up_RIGHT, action_key_down_UP, action_key_up_UP
    action_key_down_RIGHT = ActionChains(driver).key_down(Keys.ARROW_RIGHT)
    action_key_up_RIGHT= ActionChains(driver).key_up(Keys.ARROW_RIGHT)
    action_key_down_UP = ActionChains(driver).key_down(Keys.SPACE)
    action_key_up_UP = ActionChains(driver).key_up(Keys.SPACE)
    t.sleep(1)
    performkeys(action_key_up_RIGHT,action_key_down_RIGHT,1.9)
    performkeys(action_key_up_UP,action_key_down_UP,1)
    ActionChains(driver)\
            .send_keys("A")\
            .perform()

def performkeys(keyup,keydown,delay):
    endtime = t.time() + delay
    while True:
        keydown.perform()

        if t.time() > endtime:
            keyup.perform()
            break
#2.5 
#0.75
#A