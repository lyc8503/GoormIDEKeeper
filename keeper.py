from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import threading


chrome_options = Options()
options = ['--disable-gpu', '--disable-impl-side-painting', '--disable-gpu-sandbox',
           '--disable-accelerated-2d-canvas', '--disable-accelerated-jpeg-decoding', '--no-sandbox',
           '--test-type=ui']

for opt in options:
    chrome_options.add_argument(opt)

d = webdriver.Chrome(options=chrome_options)
d2 = webdriver.Chrome(options=chrome_options)


def login(name, email, password, driver):
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    driver.get('https://accounts.goorm.io/login')
    driver.find_element_by_xpath('//*[@id="emailInput"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="app"]/section/div[5]/button').click()
    while "goorm-main" not in driver.current_url:
        time.sleep(1)
    time.sleep(1)
    driver.get("https://ide-run.goorm.io/terminal/" + name + "?language=us")
    while True:
        try:
            driver.find_element_by_xpath('//*[contains(@id,"g_window_")]/div/div')
            time.sleep(5)
            break
        except:
            print("页面正在加载...")
    while True:
        driver.find_element_by_xpath('//*[contains(@id,"g_window_")]/div/div').send_keys("ls\n")
        time.sleep(5)
        print("成功输入...")


login("vpobspdt", "6ultc8sk@groupbuff.com", "@7xH3mT1sW2xY3pD0vQ7yS9gL", d)
