import time
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
    df_client_informations = pd.DataFrame(
        columns=[
            "Nome",
            "Marca",
            "Modelo",
            "Usuário Desde",
            "Telefone",
            "Preço",
            "Ano",
            "Quilometragem",
            "Potência",
            "Combustivo",
            "Kit GNV",
            "Câmbio",
            "Cor",
            "Portas",
            "Direção",
            "Aceita Trocas",
            "Endereço",
        ]
    )

    # Creates a chrome driver instance and goes to the Olx car url
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        f"https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{search_infos['brand']}/{search_infos['model']}/estado-df"
    )
    # ?me={search_infos['maxKm']}&ms={search_infos['minKm']}&re={search_infos['maxYear']}&rs={search_infos['minYear']}
    # Saves the main tab, with all the Announces
    olx_main_tab = driver.current_window_handle
    logging.info("Chrome foi aberto na página do OLX")

    # Gets the number of Announces found and splits the string to get the correct number
    options_found = driver.find_element(
        By.CSS_SELECTOR, "#main-content > div.olx-d-flex.olx-jc-space-between > div > p"
    ).text
    print(options_found)
    first_value = options_found.split(" - ")
    middle_value = first_value[1].split(" de")[0]

    # Makes a loop based on the number of Announces found
    for announces_number in range(1, int(middle_value) + 5, 1):
        # if the div is an advertisements , it skips
        if announces_number in [11, 22, 33, 44]:
            continue
        # if its not an advertisement, click it to open the
        try:
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (
                        By.CSS_SELECTOR,
                        f"#main-content > div.sc-74d68375-2.fsgdKo > section:nth-child({announces_number})",
                    )
                )
            ).click()

            # Changes the browser tab to go into the advertisement info
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            user_since = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.dBnjzp > div.ad__sc-h3us20-6.bwBaLM > div > div > div > div.sc-gEvEer.sc-jnOGJG.fPFnoJ.bwWeeV > div.sc-gEvEer.sc-dZoequ.fPFnoJ.hVyURs > div.sc-gEvEer.sc-eZkCL.fPFnoJ.miRdz > div:nth-child(3) > div > span.sc-eqUAAy.crJkyb.sc-ibQAlb.lUVuq",
            ).text
            time.sleep(3)
            driver.close()

            driver.switch_to.window(olx_main_tab)
            print(f"{user_since}")
        except Exception as err:
            logging.info("Falha ao buscar carro %s", err)
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
