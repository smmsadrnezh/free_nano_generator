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

nano_address = "nano_1d8xhr8tj56ee6xhynt3k3jqecetpdznyibx9f531w5pf7rj9oqjkrnxq48t"
refresh_rate = 15 * 60

current_path = pathlib.Path(__file__).parent.resolve()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")  # this
chrome_options.add_argument("--disable-dev-shm-using")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument(r"user-data-dir=.\cookies\\test")
driver = webdriver.Chrome(current_path / 'chromedriver', chrome_options=chrome_options)  # ChromeDriver 94.0.4606.61
driver.get("https://freenanofaucet.com")

i = 0
with open('log.csv', mode='a') as log_file:
    log_writer = csv.writer(log_file, delimiter=',')
    log_writer.writerow([i, time.strftime("%H:%M:%S", time.localtime())])
    while True:
        i += 1
        input_element = driver.find_element_by_id("nanoAddr")
        send_item = driver.find_element_by_id("getNano")
        input_element.send_keys(nano_address)
        send_item.click()
        time.sleep(refresh_rate)
        driver.back()
