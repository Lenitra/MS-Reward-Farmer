
from selenium import webdriver
import time

print("Ouverture d'un navigateur en mode mobile")
userAgent = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
profile = webdriver.ChromeOptions()
profile.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=profile)
driver.set_window_size(414, 896)

driver.get("https://lenitra.github.io/MS-Reward-Farmer/")
while True:
    print()
