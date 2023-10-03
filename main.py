import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# display
from pyvirtualdisplay import Display


import time


POINTS_COUNTER = 0




def findelement(driver, by, value):
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            continue
    return element


def waitload(driver, oldpage):
    while driver.current_url == oldpage:
        print("waiting for page to load")
        time.sleep(1)
        

# se connecte à microsoft 
def login(driver):

    driver.get("https://login.microsoftonline.com/")
    # attend que la page se charge
    findelement(driver, "name", "loginfmt").send_keys(username) # entre le nom d'utilisateur
    findelement(driver, "name", "loginfmt").send_keys(u'\ue007') # valide le nom d'utilisateur
    oldpage = driver.current_url # récupère l'url de la page actuelle

    waitload(driver, oldpage)

    oldpage = driver.current_url # récupère l'url de la page actuelle
    findelement(driver, "name", "passwd").send_keys(password) # entre le mot de passe
    findelement(driver, "name", "passwd").send_keys(u'\ue007') # valide le mot de passe
    waitload(driver, oldpage)

    # get the active element
    element = driver.switch_to.active_element
    element.send_keys(u'\ue007') # clique sur le bouton "se souvenir de moi"
    print("Connecté au compte : " + username)

    
def shearchs(driver):


    login(driver)
    # get the actual path to the python file
    for i in range(0, 30):
        rdmchar = os.urandom(8).hex()
        driver.get("https://www.bing.com/search?q=" + rdmchar)
        time.sleep(1)
    
    
    time.sleep(120)

    driver.quit()

# Type = 0 : PC
# Type = 1 : Mobile
def setdriver(type):
    options = Options()
    if type == 0: # MODE PC
        driver = webdriver.Chrome()
        driver.set_window_size(1080, 720)

    elif type == 1: # MODE MOBILE
            # get the driver size
        mobile_emulation = {
        "deviceMetrics": {
            "width": 360,
            "height": 640,
            "pixelRatio": 3.0,
        },
        "userAgent": "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
        }
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(360, 640)


    return driver



with open('accounts.json') as json_file:
    data = json.load(json_file)
    username = data[0]['username']
    password = data[0]['password']





# shearchs(setdriver(0))

display = Display(visible=0, size=(720, 360))
shearchs(setdriver(1))
display.stop()



