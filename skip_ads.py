import undetected_chromedriver as uc
import threading
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DELAY = 10

skip_ads_path = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button'

def get_driver():
    threadLocal = threading.local()
    driver = getattr(threadLocal, 'driver', None)
    if driver is None:
        options = uc.ChromeOptions()
        options.headless=False
        # options.add_argument('--headless')
        driver = uc.Chrome(options=options)
        setattr(threadLocal, 'driver', driver)

    return driver

if __name__ == '__main__':
    driver = get_driver()
    driver.get('http://www.youtube.com/')

    while True:
        time.sleep(8)
        try:            
            driver.find_element(By.XPATH, skip_ads_path).click()
            print("Skipping ad...")
        except:
            print("No ad...")
            continue