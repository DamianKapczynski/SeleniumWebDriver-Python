from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

for i in range (100):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date + " Uruchomienie nr " + str(i))
    # Open browser
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options = chrome_options)

    # Open page
    driver.get("https://nakarmpsa.olx.pl/")
    time.sleep(2)

    # Push Nakarm psa button
    button_locator = driver.find_element(By.XPATH, "/html//div[@id='pet-diana']//div[@class='single-pet-control-feed_button']/span[.='Nakarm psa']")
    button_locator.click()
    time.sleep(1)
    driver.quit()


