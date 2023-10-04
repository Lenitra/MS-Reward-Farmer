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
    print("Connexion à microsoft")
    login(driver)
    driver.get("https://lenitra.github.io/MS-Reward-Farmer/")
    print("Connecté à la page de recherche")
    print("Attente de 2 minutes")
    time.sleep(120)
    print("Fin des recherches")
    driver.quit()

# Type = 0 : PC
# Type = 1 : Mobile
def setdriver(type):
    options = Options()
    if type == 0: # MODE PC
        print("Ouverture d'un navigateur en mode PC")
        driver = webdriver.Chrome()
        driver.set_window_size(1080, 720)

    elif type == 1: # MODE MOBILE
        print("Ouverture d'un navigateur en mode mobile")

        userAgent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        profile = webdriver.ChromeOptions()
        profile.add_argument(f'user-agent={userAgent}')
        
        profile.add_experimental_option("mobileEmulation", {"deviceName": "Samsung Galaxy S8+"})

        driver = webdriver.Chrome(options=profile)
        driver.set_window_size(414, 896)


    return driver



with open('accounts.json') as json_file:
    data = json.load(json_file)
    username = data[0]['username']
    password = data[0]['password']
    for p in data:

        # display = Display(visible=0, size=(1080, 720))
        # display.start()
        shearchs(setdriver(1))
        # shearchs(setdriver(0))
        # display.stop()



