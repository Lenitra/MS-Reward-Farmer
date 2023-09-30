import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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

    driver.get("C:\\Users\\thoma\\Desktop\\MS-Reward-Farmer\\recherches.html")
    
    
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
        mobile_emulation = { "deviceName": "Pixel 5" }
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"

        # Utiliser CDP pour modifier l'agent utilisateur

        driver = webdriver.Chrome(options=options)
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": user_agent})
        driver.set_window_size(200, 720)

    return driver



with open('accounts.json') as json_file:
    data = json.load(json_file)
    username = data[0]['username']
    password = data[0]['password']





shearchs(setdriver(0))
shearchs(setdriver(1))





input("Press Enter to continue...")
