"""
Install dependencies:

```
apt install -y chromium-browser
apt install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
```
"""

import csv
import time
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

nano_address = "nano_1d8xhr8tj56ee6xhynt3k3jqecetpdznyibx9f531w5pf7rj9oqjkrnxq48t"
refresh_rate = 15 * 60

current_path = pathlib.Path(__file__).parent.resolve()

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-using")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument('--headless')
driver = webdriver.Chrome(current_path / 'chromedriver', options=options)  # ChromeDriver 94.0.4606.61
driver.get("https://freenanofaucet.com")

i = 0
with open('log.csv', mode='a') as log_file:
    while True:
        i += 1
        log_line = [i, time.strftime("%H:%M:%S", time.localtime())]
        log_writer = csv.writer(log_file, delimiter=',')
        log_row = [i, time.strftime("%H:%M:%S", time.localtime())]
        log_writer.writerow(log_row)
        print(log_row)

        input_element = driver.find_element_by_id("nanoAddr")
        send_item = driver.find_element_by_id("getNano")
        input_element.send_keys(nano_address)
        send_item.click()
        time.sleep(refresh_rate)
        driver.back()
