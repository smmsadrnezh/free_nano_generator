import csv
import time
import pathlib
from selenium import webdriver

nano_address = "nano_1d8xhr8tj56ee6xhynt3k3jqecetpdznyibx9f531w5pf7rj9oqjkrnxq48t"
refresh_rate = 15 * 60

current_path = pathlib.Path(__file__).parent.resolve()
driver = webdriver.Chrome(current_path / 'chromedriver')
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
