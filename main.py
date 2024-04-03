from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="C:/Development/chromedriver.exe")
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# I have to study CSS selectors more !!!!!!!!!!!!!!!!!!!!!!!!!!!

# driver.get("https://www.amazon.com/Kingston-500G-2280-Internal-SNV2S/dp/B0BBWJH1P8/ref=sr_1_1_sspa?crid=19ZWUS9R5UZJL&keywords=ssd%2B500gb%2Bkingston&qid=1689969714&sprefix=ssd%2B500gb%2Bkin%2Caps%2C358&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

# price = driver.find_element(By.CSS_SELECTOR, "span.a-price")
# price_again = driver.find_element(By.CLASS_NAME, "a-price")
# print(price.text)
# print(price_again.text)

# price_whole = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
# price_fraction = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]')
# print(price_whole.text + "." + price_fraction.text)

# driver.get("https://www.python.org/")
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
#
# for name in event_names:
#     print(name.text)
#
# for time in event_times:
#     print(time.text)
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text
#     }
#
# print(events)
#
# events_2 = [
#     {"time": event_time.text, "name": event_name.text}
#     for event_time, event_name in zip(event_times, event_names)
# ]
#
# print(events_2)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
#
# article_count.click()

# community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# community_portal.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# time.sleep(5)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# fname = driver.find_element(By.NAME, "fName")
# lname = driver.find_element(By.NAME, "lName")
# email = driver.find_element(By.NAME, "email")
# fname.send_keys("Hashitha")
# lname.send_keys("Mihiran")
# email.send_keys("kanthiwijesinghe71@gmail.com")
# btn = driver.find_element(By.CSS_SELECTOR, ".btn")
# btn.click()

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]  # Here also same sequence problem ???

        money_element = driver.find_element(By.CSS_SELECTOR, "#money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id  # Here when we create a dictionary we have used a = sign. How ??????? And this is not a dictionary it is a sequence

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(f"Highest affordable upgrade = {highest_price_affordable_upgrade}")
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        print(to_purchase_id)

        driver.find_element(By.CSS_SELECTOR, f"#{to_purchase_id}").click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.CSS_SELECTOR, "#cps").text
        print(f"Cookies per second = {cookie_per_s}")
        break

# driver.close()
driver.quit()

