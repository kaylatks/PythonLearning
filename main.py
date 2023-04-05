from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt



#set the chrome using the latest chrome version
service= Service('C:\\Users\\user\\Downloads\\chromedriver.exe')

def get_driver():
    #set options to make browsing easier
    options = webdriver.ChromeOptions()
    # to diable the info bar pop up when driver is runnung
    options.add_argument("disable-infobars")
    # to start the browser in maximized
    options.add_argument("start-maximized")
    # to avoid particular issue when you interact with a browser on a Linux
    options.add_argument("disable-dev-shm-usage")
    # to add sandboxing disbaled, to have greater privileges that the script is going to access and scrape
    options.add_argument("no-sandbox")
    # to avoid detection from browser because some browser dont like script so we enable our script to enable those browser
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AUtomationControlled")

    driver = webdriver.Chrome(service=service,options=options)
    # driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def WriteFile(text):
    """"Write input text into a text file"""""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename,'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    driver.find_element(by="id",value="id_username").send_keys("automated")
    time.sleep(2)
    #Keys.RETURN is pressing enter in keyboard
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    while True:
        time.sleep(2)
        timer = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]").text
        text = str(clean_text(timer))
        WriteFile(text)
    # print(driver.current_url)

print(main())

#rm *.txt
