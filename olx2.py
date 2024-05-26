import time
import random
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def main(search_infos):
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()))
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )
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

    df_ad_info = pd.DataFrame(
        columns=[
            "user_since",
            "car_price",
            "average_price",
            "fipe_price",
            "car_year",
            "car_power",
            "car_color",
            "seller_name",
            "ad_date",
            "ad_description",
        ]
    )

    # ad_number = 1
    # while ad_number <= int(page_ads) + 6:
    #     # for ad_number in range(1, int(page_ads) + 7, 1):
    #     count = 0
    #     ads_to_be_open = random.randint(1, 10)
    #     print(f"Ads to be open: {ads_to_be_open}")
    #     # for rand_iteration in range(1,ads_to_be_open):
    #     while count < ads_to_be_open:
    #         # Unwanted ads
    #         if ad_number in [4, 7, 13, 24, 35, 46]:
    #             continue
    #
    #         print(f"Ad Number: {ad_number}")
    #
    #         WebDriverWait(driver, 30).until(
    #             EC.element_to_be_clickable(
    #                 (
    #                     By.CSS_SELECTOR,
    #                     f"#main-content > div.sc-f431cc3e-2.bBwRRe > section:nth-child({ad_number}) > a",
    #                 )
    #             )
    #         ).click()
    #         wait_random_time(7, 14)
    #         driver.switch_to.window(olx_main_tab)
    #         wait_random_time(7, 14)
    #
    #         count = count + 1
    #         ad_number = ad_number + 1
    wait_random_time(3, 5)

    central_div = driver.find_element(
        By.CSS_SELECTOR,
        "# main-content > div.sc-f431cc3e-2.bBwRRe",
    )

    print(central_div)

    a_tags = central_div.find_elements_by_tag_name("section")

    # Iterate over the found <a> tags and print their attributes or text
    for a_tag in a_tags:
        print(a_tag)
        # print("Link Text:", a_tag.text)
        # print("Link Href:", a_tag.get_attribute("href"))

    # for ad_number in range(1, int(page_ads) + 7, 1):
    #     # Unwanted ads
    #     if ad_number in [4, 7, 13, 24, 35, 46]:
    #         continue
    #     try:
    #         WebDriverWait(driver, 30).until(
    #             EC.element_to_be_clickable(
    #                 (
    #                     By.CSS_SELECTOR,
    #                     f"#main-content > div.sc-f431cc3e-2.bBwRRe > section:nth-child({ad_number}) > a",
    #                 )
    #             )
    #         ).click()
    #         wait_random_time(5, 10)
    #         driver.switch_to.window(driver.window_handles[1])
    #
    #         # Gets how old the seller is on OLX
    #         user_since = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.dBnjzp > div.ad__sc-h3us20-6.bwBaLM > div > div > div > div.sc-gEvEer.sc-jnOGJG.fPFnoJ.bwWeeV > div.sc-gEvEer.sc-dZoequ.fPFnoJ.hVyURs > div.sc-gEvEer.sc-eZkCL.fPFnoJ.miRdz > div:nth-child(3) > div > span.sc-eqUAAy.crJkyb.sc-ibQAlb.lUVuq",
    #         )
    #         if user_since:
    #             user_since = user_since.text
    #         else:
    #             print("Unable to fetch 'user since'")
    #             user_since = None
    #
    #         # Gets the car price
    #         car_price = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.hQZMji > div > div > div > div.ad__sc-en9h1n-0.IoqnP > div.ad__sc-1leoitd-2.fIICfM.olx-d-flex.olx-ai-flex-start.olx-fd-column > h2",
    #         )
    #         if car_price:
    #             car_price = car_price.text
    #         else:
    #             print("Unable to fetch car price")
    #             car_price = None
    #
    #         # Gets the average car price on OLX
    #         average_price = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.fnDpgM > div > div > div > div.sc-bcXHqe.sc-eDvSVe.caEdXs.hKQPaV > div:nth-child(1) > div.sc-bcXHqe.DqRAg > span",
    #         )
    #         if average_price:
    #             average_price = average_price.text
    #         else:
    #             print("Unable to fetch car average price on OLX")
    #             average_price = None
    #
    #         # Gets the FIPE price of the car
    #         fipe_price = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.fnDpgM > div > div > div > div.sc-bcXHqe.sc-eDvSVe.caEdXs.hKQPaV > div:nth-child(2) > div > span",
    #         )
    #         if fipe_price:
    #             fipe_price = fipe_price.text
    #         else:
    #             print("Unable to fetch FIPE PRICE")
    #             fipe_price = None
    #
    #         # Gets the car year
    #         car_year = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(5) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > a",
    #         )
    #         if car_year:
    #             car_year = car_year.text
    #         else:
    #             print("Unable to fetch car year")
    #             car_year = None
    #
    #         # Gets the car power
    #         car_power = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(7) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
    #         )
    #         if car_power:
    #             car_power = car_power.text
    #         else:
    #             print("Unable to fetch car power")
    #             car_power = None
    #
    #         # Gets the car power
    #         car_color = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(11) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
    #         )
    #         if car_color:
    #             car_color = car_color.text
    #         else:
    #             print("Unable to fetch car color")
    #             car_color = None
    #
    #         # Gets the seller name
    #         seller_name = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.dBnjzp > div.ad__sc-h3us20-6.bwBaLM > div > div > div > div.sc-gEvEer.sc-jnOGJG.fPFnoJ.bwWeeV > div.sc-gEvEer.sc-dZoequ.fPFnoJ.hVyURs > div.sc-gEvEer.sc-bBeLUv.fPFnoJ.ebacRy > div > div > div > div > span",
    #         )
    #         if seller_name:
    #             seller_name = seller_name.text
    #         else:
    #             print("Unable to fetch car color")
    #             seller_name = None
    #
    #         # Gets the ad date
    #         ad_date = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ckBKfA > div > div > div > span.olx-text.olx-text--caption.olx-text--block.olx-text--regular.ad__sc-1oq8jzc-0.dWayMW.olx-color-neutral-120",
    #         )
    #         if ad_date:
    #             ad_date = ad_date.text
    #         else:
    #             print("Unable to fetch ad date")
    #             ad_date = None
    #
    #         # Gets the ad description
    #         ad_description = driver.find_element(
    #             By.CSS_SELECTOR,
    #             "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.hqQzeT > div > div > div > div.ad__sc-1sj3nln-0.focuCb > div > p > span",
    #         )
    #         if ad_description:
    #             ad_description = ad_description.text
    #         else:
    #             print("Unable to fetch ad date")
    #             ad_description = None
    #
    #         suitable_seller = []
    #         new_row = {
    #             "user_since": user_since,
    #             "car_price": car_price,
    #             "average_price": average_price,
    #             "fipe_price": fipe_price,
    #             "car_year": car_year,
    #             "car_power": car_power,
    #             "car_color": car_color,
    #             "seller_name": seller_name,
    #             "ad_date": ad_date,
    #             "ad_description": ad_description,
    #         }
    #         print(new_row)
    #         suitable_seller.append(new_row)
    #
    #         df_ad_info = pd.concat([df_ad_info, pd.DataFrame(suitable_seller)])
    #         print(df_ad_info)
    #         # time.sleep(1200)
    #         wait_random_time(5, 50)
    #         driver.close()
    #         driver.switch_to.window(olx_main_tab)
    #         wait_random_time()
    #         print(f"Ad {ad_number} crawled")
    #     except Exception as err:
    #         print(f"Impossible to go to ad {ad_number} switch")


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
