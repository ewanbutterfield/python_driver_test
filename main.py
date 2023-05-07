from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from enum import Enum

driver = webdriver.Chrome()


class Stores(Enum):
    no_frills = "https://www.nofrills.ca/"
    save_on_foods = "https://www.saveonfoods.com/sm/pickup/rsid/1982/"
    superstore = "https://www.realcanadiansuperstore.ca/"
    urban_fare = "https://www.urbanfare.com/sm/pickup/rsid/7615/"


# iga is just the worst and doesn't work when the rest do
#    iga = "https://www.iga.net/en"


def main():
    # Use a breakpoint in the code line below to debug your script.
    search_all_stores("Bread")
    time.sleep(60)
    driver.quit()


def search_product(store_url, product_keywords):
    driver.switch_to.new_window('tab')
    driver.get(store_url)
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    search_bar.click()
    search_bar.clear()
    search_bar.send_keys(product_keywords)
    search_bar.send_keys(Keys.RETURN)


def search_all_stores(product_keywords):
    for store in Stores:
        search_product(store.value, product_keywords)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
