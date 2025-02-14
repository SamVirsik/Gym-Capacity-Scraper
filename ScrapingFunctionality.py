try:
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup
    #import re

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup

    import csv
    from datetime import datetime


    url = "https://recwell.berkeley.edu/facilities/recreational-sports-facility-rsf/rsf-weight-room-crowd-meter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    primary_div = soup.find_all('div', id = 'primary')[0]
    main_div = primary_div.find('main')
    ps = main_div.find_all('p')
    newlink = ps[5].find("iframe").get('src')

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(newlink)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.styles_waitTimeFullnessWrapper__3PRdQ"))
        )
    except Exception as e:
        print("Error waiting for element:", e)
        driver.quit()
        exit()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    span = soup.find('div', class_ = 'styles_waitTimeFullnessWrapper__3PRdQ').find('span')
    text = span.get_text()
    value = text[0:text.find(r'%')]


    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    csv_file_path = r'C:\Users\samvi\Documents\Coding Projects\RSF Scraper\RSF_Data.csv'
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, value])
        print("RSF is currently " + value + r"% full.")

except:
    pass