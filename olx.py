import os
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    filename="histórico_de_acoes.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


def olx_webcrawler(search_infos):
    "WebScrapping for downloading cars selling in Olx"

    # Creates a dataframe to add the info gotten
    df_client_informations = pd.DataFrame()

    # Creates a chrome driver instance and goes to the Olx car url
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        f"https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{search_infos['brand']}/{search_infos['model']}/estado-df?me={search_infos['maxKm']}&ms={search_infos['minKm']}&re={search_infos['maxYear']-150}&rs={search_infos['minYear']-150}"
    )

    # Saves the main tab, with all the advertisements
    olx_main_tab = driver.current_window_handle
    logging.info("Chrome foi aberto na página do OLX")

    # Gets the number of adversings found and splits the string to get the correct number
    options_found = driver.find_element(
        By.CSS_SELECTOR, "#main-content > div.olx-d-flex.olx-jc-space-between > div > p"
    ).text
    print(options_found)
    first_value = options_found.split(" - ")
    middle_value = first_value[1].split(" de")[0]

    # Makes a loop based on the number of advertisements found
    for advertisement_number in range(1, int(middle_value) + 5, 1):
        if advertisement_number in [11, 22, 33, 44]:
            continue
        options_found = driver.find_element(
            By.CSS_SELECTOR,
            f"#main-content > div.sc-74d68375-2.fsgdKo > section:nth-child({advertisement_number})",
        ).click()
        driver.switch_to.window(driver.window_handles[1])

        print(f"teste{advertisement_number}")
    driver.close()
    return


dicionario_exemplo = {
    "brand": "audi",
    "model": "a3",
    "minKm": 0,
    "maxKm": 500000,
    "minYear": 0,
    "maxYear": 74,
}

olx_webcrawler(dicionario_exemplo)
