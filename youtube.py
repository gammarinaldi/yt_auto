import undetected_chromedriver as uc
import threading
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent

DELAY = 10 # seconds

login_url = 'https://accounts.google.com'
homepage_url = 'https://www.youtube.com/'
login_btn = '//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div'
email_input = '//input[@id="identifierId"]'
pass_input = '//input[@name="Passwd"]'
next_btn = '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl3Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]'
playlist_urls = [
        'https://www.youtube.com/playlist?list=PLFxJN8xu8qvX41ye5NCpdjqd0QGR_hjiq',
        # 'https://www.youtube.com/playlist?list=PL1-o1Gx_tWA0iFkjbRdzryqajkDh1hvli'
    ]
play_all_btn = '//*[@id="page-manager"]/ytd-browse/ytd-playlist-header-renderer/div/div[3]/div[1]/div/div[3]/ytd-button-renderer[1]/yt-button-shape/a/yt-touch-feedback-shape/div'
open_yt_profile_btn = '//*[@id="avatar-btn"]'
open_acc_profile_btn = '//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a'
logout_btn = '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[3]/ytd-compact-link-renderer[4]'
my_activity_url = 'https://myactivity.google.com/product/youtube?pli=1'
delete_history_btn = '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-Bz113c-UbuQg VfPpkd-LgbsSe-OWXEXe-dgl3Hf Rj3Mlf OLiIxf PDpWxe LQeN7 fMgR5d"]'
delete_history_all_time_btn = "//li[@data-action='aqC7Rd']"
confirm_delete_history_btn = '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ nCP5yc AjY5Oe DuMIQc LQeN7 e6p9Rc"]'
# video_url = f'youtube.com/watch?app={platform}&v=QqYzGFsqxRc'
# video_url = f'youtube.com/watch?app={platform}&v=aIkWDY6QbX0'
skip_ads_path = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[3]/div/div/ytd-player/div/div/div[17]/div/div[3]/div/div[3]/span/button'

def users_path():
    return r'C:\Users\Gama\Desktop\yt_auto\users1.json'

def get_driver():
    threadLocal = threading.local()
    driver = getattr(threadLocal, 'driver', None)
    if driver is None:
        chrome_options = uc.ChromeOptions()

        # All arguments to hide robot automation trackers
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-service-autorun")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        ua = UserAgent()
        userAgent = ua.random
        print(userAgent)
        chrome_options.add_argument(f'--user-agent={userAgent}')

        driver = uc.Chrome(options=chrome_options, port=9000)

        setattr(threadLocal, 'driver', driver)

    return driver

def get_users():
    f = open(users_path())
    users = json.load(f)
    f.close()

    return users

def open_login(driver):
    driver.get(login_url)

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

def play_one(driver):
    driver.get(video_url)

def open_yt_profile(email, driver):
    try:
        print("Try click youtube profile")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, open_yt_profile_btn)))
        driver.find_element(By.XPATH, open_yt_profile_btn).click()
    except TimeoutException:
        msg = email + ": click youtube profile failed!"
        print(msg)

def open_acc_profile(email, driver):
    try:
        print("Try click account profile")
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, open_acc_profile_btn)))
        driver.find_element(By.XPATH, open_acc_profile_btn).click()
    except TimeoutException:
        msg = email + ": click account profile failed!"
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
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, f'//*[text()="{email}"]')))
        return True
    except TimeoutException:
        return False

def delete_cache(driver):
    # Create a separate tab than the main one
    driver.execute_script("window.open('')")

    # Switch window to the second tab
    driver.switch_to.window(driver.window_handles[-1])

    # Open your chrome settings.
    driver.get('chrome://settings/clearBrowserData')

    # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
    perform_delete_cache(driver, Keys.TAB * 3 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)

    driver.close()

def perform_delete_cache(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(3)
    actions.perform()

def write_txt(email):
    with open('failed.txt', 'a') as fd:
        fd.write(f'\n{email}')

def call(user, url):
    email = user['email']
    password = user['password']
    driver = get_driver()

    print(email + ": Open login page")
    open_login(driver)

    time.sleep(3)

    print(email + ": Input email")
    input_email(email, driver)

    time.sleep(3)

    print(email + ": Input password")
    input_pass(email, password, driver)

    time.sleep(3)

    print(email + ": Open account profile")
    open_acc_profile(email, driver)

    time.sleep(3)

    if check_login(email, driver):
        msg = email + ": login success!"
        print(msg)
        time.sleep(3)

        print(email + ": Open playlist")
        open_playlist(driver, url)

        time.sleep(3)
        
        print(email + ": Play all")
        play_all(email, driver)

        # # print("Play single video")
        # # play_one(driver)

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

        # time.sleep(3)

        # print(email + ": Open youtube homepage")
        # open_homepage(driver)

        # time.sleep(3)

        # print(email + ": Open profile")
        # open_yt_profile(email, driver)

        # time.sleep(3)

        # print(email + ": Logout")
        # logout(email, driver)

        time.sleep(3)

        # print(email + ": Clear browser cache")
        # delete_cache(driver)
    else:
        msg = email + ": login failed!"
        print(msg)
        write_txt(email)

    driver.close()

if __name__ == '__main__':
    for url in playlist_urls:  
        for user in get_users():
            call(user, url)
