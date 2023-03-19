from selenium import webdriver

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

    driver = webdriver.Chrome(options)
