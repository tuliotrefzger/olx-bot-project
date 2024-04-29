import time
import random
import pprint
import datetime

# import pandas as pd
import pyautogui
import undetected_chromedriver as uc
import pyscreeze

from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False


def get_driver():
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()))
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
    driver.maximize_window()
    return driver


def wait_based_on_iteration(iteration):
    if iteration % 16 == 0:
        wait_random_time(60, 80)
    elif iteration % 25 == 0:
        wait_random_time(90, 110)
    else:
        wait_random_time(10, 20)


def wait_random_time(min_time=3, max_time=6):
    # Generate a random time between 3 and 6 seconds
    random_time = random.uniform(min_time, max_time)

    # Waits a random time
    time.sleep(random_time)


def get_urls(driver):
    menu_page = BeautifulSoup(driver.page_source, "lxml")

    with open("menu_page.html", "w", encoding="utf-8") as file:
        file.write(menu_page.prettify())

    a_tags = menu_page.find_all("a", attrs={"data-ds-component": "DS-NewAdCard-Link"})
    links_set = set([])
    for a_tag in a_tags:
        href_value = a_tag.get("href")
        if "autos-e-pecas" in href_value:
            links_set.add(href_value)
    pprint.pprint(links_set)

    return links_set


def get_car_price(ad_page, url):
    price_tag = ad_page.find(
        "h2",
        class_="olx-text olx-text--title-large olx-text--block ad__sc-1leoitd-0 bJHaGt",
    )
    if price_tag:
        return price_tag.text

    print(f"Price wasnt found for URL: {url}")
    return None


def get_user_since(ad_page, url):
    user_since_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.dBnjzp > div.ad__sc-h3us20-6.bwBaLM > div > div > div > div.sc-gEvEer.sc-jnOGJG.fPFnoJ.bwWeeV > div.sc-gEvEer.sc-dZoequ.fPFnoJ.hVyURs > div.sc-gEvEer.sc-eZkCL.fPFnoJ.miRdz > div:nth-child(3) > div > span.sc-eqUAAy.crJkyb.sc-ibQAlb.lUVuq"
    )
    if user_since_tag:
        return user_since_tag.text

    print(f"User since wasnt found for URL: {url}")
    return None


def get_average_olx_price(ad_page, url):
    average_olx_price_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.fnDpgM > div > div > div > div.sc-bcXHqe.sc-eDvSVe.caEdXs.hKQPaV > div:nth-child(1) > div.sc-bcXHqe.DqRAg > span"
    )
    if average_olx_price_tag:
        return average_olx_price_tag.text

    print(f"Average OLX price wasnt found for URL: {url}")
    return None


def get_fipe_price(ad_page, url):
    fipe_price_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.fnDpgM > div > div > div > div.sc-bcXHqe.sc-eDvSVe.caEdXs.hKQPaV > div:nth-child(2) > div > span"
    )
    if fipe_price_tag:
        return fipe_price_tag.text

    print(f"FIPE price wasnt found for URL: {url}")
    return None


def get_car_model(ad_page, url):
    model_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(2) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > a"
    )
    if model_tag:
        return model_tag.text

    print(f"Model specification wasnt found for URL: {url}")
    return None


def get_car_year(ad_page, url):
    car_year_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(5) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > a"
    )
    if car_year_tag:
        return car_year_tag.text

    print(f"Car year wasnt found for URL: {url}")
    return None


def get_car_color(ad_page, url):
    car_color_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(11) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130"
    )
    if car_color_tag:
        return car_color_tag.text

    print(f"Car color wasnt found for URL: {url}")
    return None


def get_car_km(ad_page, url):
    car_km_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(6) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130"
    )
    if car_km_tag:
        return car_km_tag.text

    print(f"Car km wasnt found for URL: {url}")
    return None


def get_ad_publish_date(ad_page, url):
    published_at_tag = ad_page.select_one(
        "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ckBKfA > div > div > div > span.olx-text.olx-text--caption.olx-text--block.olx-text--regular.ad__sc-1oq8jzc-0.dWayMW.olx-color-neutral-120"
    )
    if published_at_tag:
        return published_at_tag.text

    print(f"Ad published date wasnt found for URL: {url}")
    return None


def currency_to_number(currency_string):
    """
    This function takes a string representing a currency value and removes the currency symbol and formatting to return the integer value.

    Args:
        currency_string: A string representation of a currency value. (e.g., "R$ 100.000")

    Returns:
        The integer value of the currency string without decimals. (e.g., 100000)
    """
    # Remove all characters except numbers, ",", "+" or "-".
    numbers = "".join(
        char for char in currency_string if char.isdigit() or char in ",+-"
    )
    # Split the string at the decimal point (if it exists)
    split_string = numbers.split(",")
    # Use only the integer part (index 0) and convert to integer
    return int(split_string[0])


def login(driver):
    driver.get("https://www.olx.com.br")
    # Login part
    try:
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#header > nav > div > div.olx-header__column-right > ul > li.olx-header__profile-item > a",
                )
            )
        ).click()
        wait_random_time()
        # time.sleep(120)
        time.sleep(60)
        driver.refresh()
        wait_random_time()
    except Exception as err:
        print("Impossible to find login button")


def get_cars(driver, search_infos):
    driver.get(
        f"https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{search_infos['brand']}/{search_infos['model']}/estado-df?f=p&me={search_infos['maxKm']}&ms={search_infos['minKm']}&re={search_infos['maxYear']}&rs={search_infos['minYear']}"
    )

    ad_urls = get_urls(driver)
    count = 0
    for car_url in ad_urls:
        count = count + 1
        print(
            f"---------------------------------------------- {count} ----------------------------------------------"
        )

        print(f"Started at: {datetime.datetime.now()}")
        driver.get(car_url)
        wait_random_time(10, 15)
        ad_page = BeautifulSoup(driver.page_source, "lxml")
        with open("ad_page.html", "w", encoding="utf-8") as file:
            file.write(ad_page.prettify())

        print(f"URL: {car_url}")

        car_price = get_car_price(ad_page, car_url)
        print(f"Price: {car_price}")

        # Skips vehicle if price was not found
        if not car_price:
            continue

        # Removes car more expensive than allowed
        if currency_to_number(car_price) > search_infos["maxPrice"]:
            print(f"Car {car_url} is more expensive than the maximum allowed price")
            continue

        fipe_price = get_fipe_price(ad_page, car_url)
        print(f"Preço FIPE: {fipe_price}")

        if fipe_price:
            if currency_to_number(car_price) < 0.85 * currency_to_number(fipe_price):
                print(
                    "This vehicle is cheaper than 85% of its FIPE price, therefore we skipped it"
                )
                continue

        average_olx_price = get_average_olx_price(ad_page, car_url)
        print(f"Preço médio OLX: {average_olx_price}")

        ad_publishment_date = get_ad_publish_date(ad_page, car_url)
        print(f"Data de publicação: {ad_publishment_date}")

        user_since = get_user_since(ad_page, car_url)
        print(f"Usuário desde: {user_since}")

        car_model = get_car_model(ad_page, car_url)
        print(f"Modelo: {car_model}")

        car_year = get_car_year(ad_page, car_url)
        print(f"Ano: {car_year}")

        car_color = get_car_color(ad_page, car_url)
        print(f"Cor: {car_color}")

        car_km = get_car_km(ad_page, car_url)
        print(f"Kilometragem: {car_km}")

        time.sleep(10)

        try:
            chat_button = "./images/chat-button-3.png"

            button_location = pyautogui.locateOnScreen(
                chat_button, confidence=0.8, grayscale=True
            )

            if button_location is not None:
                # If the button is found, get its center coordinates
                button_center = pyautogui.center(button_location)
                print(button_center)
                pyautogui.click(button_center[0], button_center[1])
                print("Chat button found at:", button_center)
            else:
                print("Chat button not found on the screen.")
                continue
        except Exception as e:
            print("Chat button not found on the screen.")
            continue

        # # -------------- Old find chat button ------------
        # chat_button = "./chat-button-3.png"
        #
        # button_location = pyautogui.locateOnScreen(
        #     chat_button, confidence=0.8, grayscale=True
        # )
        #
        # if button_location is not None:
        #     # If the button is found, get its center coordinates
        #     button_center = pyautogui.center(button_location)
        #     print(button_center)
        #     pyautogui.click(button_center[0], button_center[1])
        #     print("Chat button found at:", button_center)
        # else:
        #     print("Chat button not found on the screen.")
        #     continue

        # -------------- Send message part ------------
        try:
            input_field = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        "#input-text-message",
                    )
                )
            )

            input_field.send_keys(search_infos["message"])
            # # This part works and really sends a message. Leave commented while developing
            # input_field.send_keys(Keys.ENTER)
            wait_random_time()
        except Exception as err:
            print(f"Impossible to send message to client {car_url}")

        wait_based_on_iteration(count)

        print(f"Finished at: {datetime.datetime.now()}")


def send_olx_message_automation(search_infos):
    # create the driver object.
    driver = get_driver()

    login(driver)

    # search_infos = {
    #     "brand": "ford",
    #     "model": "ka",
    #     "minKm": 0,
    #     "maxKm": 60000,
    #     "minYear": 68,
    #     "maxYear": 74,
    #     "maxPrice": 200000,
    #     "message": "Olá, tudo bem?",
    # }

    get_cars(driver, search_infos)

    print("\nTHE END")

    # close the driver.
    driver.close()


if __name__ == "__main__":

    # create the driver object.
    driver = get_driver()

    login(driver)

    search_infos = {
        "brand": "ford",
        "model": "ka",
        "minKm": 0,
        "maxKm": 60000,
        "minYear": 68,
        "maxYear": 74,
        "maxPrice": 200000,
        "message": "Olá, tudo bem?",
    }

    get_cars(driver, search_infos)

    print("\nTHE END")

    # close the driver.
    driver.close()
