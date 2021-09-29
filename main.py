"""
Install dependencies:

```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
apt update -y
apt install -y google-chrome-stable
apt install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
```
"""

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from bs4 import BeautifulSoup

from settings import url, file_name, refresh_rate, nano_address


def initiate_chrome_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-dev-shm-using")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument('--headless')
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), options=options)
    # driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    return driver


def make_nano(driver):
    input_element = driver.find_element_by_id("nanoAddr")
    send_item = driver.find_element_by_id("getNano")
    input_element.send_keys(nano_address)
    send_item.click()
    time.sleep(5)
    return driver.page_source


def write_logs(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    element = soup.find_all("p", attrs={"class": "faucetText"})[0]
    log_row = [time.strftime("%H:%M:%S", time.localtime()), element]
    with open(file_name, mode='a') as log_file:
        log_writer = csv.writer(log_file, delimiter=',')
        log_writer.writerow(log_row)
    print(log_row)


if __name__ == '__main__':

    driver = initiate_chrome_driver()

    while True:
        html_source = make_nano(driver)
        write_logs(html_source)
        time.sleep(refresh_rate)
        driver.back()
