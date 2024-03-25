import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def main(search_infos):
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.olx.com.br")
    print(driver.current_url)
    print(driver.title)
    # # Login part
    # try:
    #     WebDriverWait(driver, 30).until(
    #         EC.element_to_be_clickable(
    #             (
    #                 By.CSS_SELECTOR,
    #                 "#header > nav > div > div.olx-header__column-right > ul > li.olx-header__profile-item > a",
    #             )
    #         )
    #     ).click()
    #     wait_random_time()
    #     time.sleep(60)
    #     # Goes back to main page
    #     driver.back()
    #     driver.back()
    #     driver.refresh()
    #     wait_random_time()
    # except Exception as err:
    #     print("Impossible to find login button")

    try:
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#main > nav.Carousel_home-carousel__HuoQB.Container_home-container__aomo5 > div > div > div > div > div:nth-child(3) > a",
                )
            )
        ).click()
        wait_random_time()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#category-selector > option:nth-child(1)",
                )
            )
        ).click()
        wait_random_time()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#location-selector > option:nth-child(8)",
                )
            )
        ).click()
        wait_random_time()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#main > section.CategoryBanner_home-category-banner__yCsN2.CategoryBanner_home-category-banner--autos-fair__bzMhV > div:nth-child(3) > div > div > a",
                )
            )
        ).click()
    except Exception as err:
        print("Impossible to get to car section")

    # Filter part
    try:
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    search_infos["brand"],
                )
            )
        ).click()
        wait_random_time()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    search_infos["model"],
                )
            )
        ).click()
        wait_random_time()
    except Exception as err:
        print("Unable to find brand and model selects")

    olx_main_tab = driver.current_window_handle
    try:
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#main-content > div.sc-9fd2daa4-0.dfRhiW > div > div > div > div > div.sc-234c68ef-0.gjQalA > div:nth-child(1) > label > span.olx-toggle-switch__stylized",
                )
            )
        ).click()
        wait_random_time()
    except Exception as err:
        print("Impossible to find 'Festival de Carros' switch")

    total_ads = 0
    page_ads = 0
    try:
        options_found = driver.find_element(
            By.CSS_SELECTOR,
            "#main-content > div.olx-d-flex.olx-jc-space-between > div > p",
        ).text
        # print(options_found)
        first_value = options_found.split(" - ")
        page_ads = first_value[1].split(" de")[0]
        print(page_ads)
        total_ads = first_value[1].split(" de")[1]
        print(total_ads)
        wait_random_time()
    except Exception as err:
        print("Impossible to find 'Festival de Carros' switch")

    for ad_number in range(1, int(page_ads) + 7, 1):
        # Unwanted ads
        if ad_number in [4, 7, 13, 24, 35, 46]:
            continue
        try:
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        f"#main-content > div.sc-f431cc3e-2.bBwRRe > section:nth-child({ad_number}) > a",
                    )
                )
            ).click()
            wait_random_time(5, 10)
            driver.switch_to.window(driver.window_handles[1])
            wait_random_time(5, 10)
            driver.close()
            driver.switch_to.window(olx_main_tab)
            wait_random_time()
            print(f"Ad {ad_number} crawled")
        except Exception as err:
            print(f"Impossible to go to ad {ad_number} switch")

    time.sleep(1200)


def wait_random_time(min_time=3, max_time=6):
    # Generate a random time between 3 and 6 seconds
    random_time = random.uniform(min_time, max_time)

    # Wait for the random time
    time.sleep(random_time)


dicionario_exemplo = {
    "brand": "AUDI",
    "model": "A3",
    "minKm": 0,
    "maxKm": 500000,
    "minYear": 0,
    "maxYear": 74,
}
main(dicionario_exemplo)
