import undetected_chromedriver as uc
import threading
import json
import time
import traceback
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

DELAY = 10 # seconds

platform = 'mobile'
homepage_url = f'https://www.youtube.com/?app={platform}'
login_btn = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div'
email_input = '//input[@id="identifierId"]'
pass_input = '//input[@name="Passwd"]'
next_btn = '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]'
playlist_urls = [
        f'https://www.youtube.com/playlist?app={platform}&list=PLFxJN8xu8qvX41ye5NCpdjqd0QGR_hjiq',
        f'https://www.youtube.com/playlist?app={platform}&list=PL1-o1Gx_tWA0iFkjbRdzryqajkDh1hvli'
    ]
play_all_btn = '//*[@id="page-manager"]/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[2]/ytd-button-renderer[1]/yt-button-shape/a/yt-touch-feedback-shape/div'
open_profile_btn = "//*[@id='avatar-btn']"
logout_btn = '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[4]'
my_activity_url = 'https://myactivity.google.com/product/youtube?pli=1'
delete_history_btn = '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-Bz112c-UbuQg VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe LQeN7 fMgR5d"]'
delete_history_all_time_btn = "//li[@data-action='aqC7Rd']"
confirm_delete_history_btn = '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ nCP5yc AjY5Oe DuMIQc LQeN7 e6p9Rc"]'
# video_url = f'https://www.youtube.com/watch?app={platform}&v=QqYzGFsqxRc'
# video_url = f'https://www.youtube.com/watch?app={platform}&v=aIkWDY6QbX0'
skip_ads_path = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[2]/span/button'

def users_path():
    return r'C:\Users\Gama\Desktop\yt_auto\users.json'

def get_driver():
    threadLocal = threading.local()
    driver = getattr(threadLocal, 'driver', None)
    if driver is None:
        chrome_options = uc.ChromeOptions()

        # All arguments to hide robot automation trackers
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-service-autorun")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")

        driver = uc.Chrome(options=chrome_options, port=9000)

        setattr(threadLocal, 'driver', driver)

    return driver

# def get_driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     # options.add_argument("--headless")

#     # Chrome is controlled by automated test software
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
#     s = Service('C:\\Users\\Gama\\Desktop\\yt_auto\\chromedriver.exe')
#     driver = webdriver.Chrome(service=s, options=options)

#     # Selenium Stealth settings
#     stealth(driver,
#             languages=["en-US", "en"],
#             vendor="Google Inc.",
#             platform="Win32",
#             webgl_vendor="Intel Inc.",
#             renderer="Intel Iris OpenGL Engine",
#             fix_hairline=True,
#             )

#     return driver

def get_users():
    f = open(users_path())
    users = json.load(f)
    f.close()

    return users

def open_homepage(driver):
    driver.get(homepage_url)

def click_login(email, driver):
    try:
        print("Try click login btn")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, login_btn)))
        driver.find_element(By.XPATH, login_btn).click()
    except TimeoutException:
        msg = email + ": click login btn failed!"
        print(msg)

def input_email(email, driver):
    try:
        print("Try input email")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, email_input)))
        eml = driver.find_element(By.XPATH, email_input)
        eml.send_keys(email)
        eml.send_keys(Keys.RETURN)
    except TimeoutException:
        msg = email + ": input email failed!"
        print(msg)

def input_pass(email, password, driver):
    try:
        print("Try input password")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, pass_input)))
        pwd = driver.find_element(By.XPATH, pass_input)
        pwd.send_keys(password)
        pwd.send_keys(Keys.RETURN)
    except TimeoutException:
        msg = email + ": input password failed!"
        print(msg)

def click_next(email, driver):
    try:
        print("Try click next")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, next_btn)))
        driver.find_element(By.XPATH, next_btn).click()
    except TimeoutException:
        msg = email + ": click next failed!"
        print(msg)

def open_playlist(driver, url):
    driver.get(url)

def play_all(email, driver):
    try:
        print("Try click play all")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, play_all_btn)))
        driver.find_element(By.XPATH, play_all_btn).click()
    except TimeoutException:
        msg = email + ": click play all failed!"
        print(msg)

def play_video(driver):
    driver.get(video_url)

def open_profile(email, driver):
    try:
        print("Try click profile")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, open_profile_btn)))
        driver.find_element(By.XPATH, open_profile_btn).click()
    except TimeoutException:
        msg = email + ": click profile failed!"
        print(msg)

def open_my_activity(driver):
    driver.get(my_activity_url)

def logout(email, driver):
    try:
        print("Try click logout")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, logout_btn)))
        driver.find_element(By.XPATH, logout_btn).click()
    except TimeoutException:
        msg = email + ": click logout failed!"
        print(msg)

def delete_history(email, driver):
    try:
        print("Try click delete history")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, delete_history_btn)))
        driver.find_element(By.XPATH, delete_history_btn).click()
    except TimeoutException:
        msg = email + ": click delete failed!"
        print(msg)

def delete_history_all_time(email, driver):
    try:
        print("Try click delete history all time")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, delete_history_all_time_btn)))
        driver.find_element(By.XPATH, delete_history_all_time_btn).click()
    except TimeoutException:
        msg = email + ": click delete history all time failed!"
        print(msg)

def confirm_delete_history(email, driver):
    try:
        print("Try click confirm delete history")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, confirm_delete_history_btn)))
        driver.find_element(By.XPATH, confirm_delete_history_btn).click()
    except TimeoutException:
        msg = email + ": click confirm delete history failed!"
        print(msg)

def skip_ads(driver):
    timeout = time.time() + 60*5   # 5 minutes from now
    while True:
        time.sleep(8)
        try:
            driver.find_element(By.XPATH, skip_ads_path).click()
        except:
            continue

        if time.time() > timeout:
            break

def check_login(email, driver):
    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, f'//*[@title="{email}"]')))
        msg = email + ": login success!"
        print(msg)
    except TimeoutException:
        msg = email + ": login failed!"
        print(msg)

def delete_cache(driver):
    # Create a separate tab than the main one
    driver.execute_script("window.open('')")

    # Switch window to the second tab
    driver.switch_to.window(driver.window_handles[-1])

    # Open your chrome settings.
    driver.get('chrome://settings/clearBrowserData')

    # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
    perform_delete_cache(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)

    driver.close()

def perform_delete_cache(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    actions.perform()

def call(user, url):
    email = user['email']
    password = user['password']
    driver = get_driver()

    print(email + ": Open youtube homepage")
    open_homepage(driver)

    time.sleep(3)

    print(email + ": Do login")
    click_login(email, driver)

    time.sleep(3)

    print(email + ": Input email")
    input_email(email, driver)

    time.sleep(3)

    print(email + ": Input password")
    input_pass(email, password, driver)

    time.sleep(3)

    print(email + ": Open youtube homepage")
    open_homepage(driver)

    time.sleep(3)

    print(email + ": Open profile")
    open_profile(email, driver)

    time.sleep(3)

    check_login(email, driver)

    time.sleep(3600)

    print(email + ": Open playlist")
    open_playlist(driver, url)

    time.sleep(3)
    
    print(email + ": Play all")
    play_all(email, driver)

    # print("Play video")
    # play_video(driver)

    print(email + ": Skip ads")
    skip_ads(driver)

    time.sleep(60*90)

    print(email + ": Open my activity")
    open_my_activity(driver)

    time.sleep(3)

    print(email + ": Click delete history")
    delete_history(email, driver)

    time.sleep(3)

    print(email + ": Click delete history all time")
    delete_history_all_time(email, driver)

    time.sleep(3)

    print(email + ": Click confirm delete history")
    confirm_delete_history(email, driver)

    time.sleep(3)

    print(email + ": Open youtube homepage")
    open_homepage(driver)

    time.sleep(3)

    print(email + ": Open profile")
    open_profile(email, driver)

    time.sleep(3)

    print(email + ": Logout")
    logout(email, driver)

    time.sleep(3)

    print(email + ": Clear browser cache")
    delete_cache(driver)

    driver.quit()

if __name__ == '__main__':
    for url in playlist_urls:  
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_user = {executor.submit(call, user, url): user for user in get_users()}
            for future in concurrent.futures.as_completed(future_to_user):
                user = future_to_user[future]
                try:
                    if future.result() == None:
                        print("Result success")
                    else:
                        print("Result failed")
                        print(future.result())
                except Exception as error:
                    print("Error occured")
                    print(error)
                    traceback.print_exc()