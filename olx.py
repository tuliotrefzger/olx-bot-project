import time
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException

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

    # Login part
    # driver.get("https://conta.olx.com.br/acesso")
    # WebDriverWait(driver, 180).until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.CSS_SELECTOR,
    #             "#header > nav > div > div.sc-eTEhWN.iJIOMF > ul > li:nth-child(6) > a",
    #         )
    #     )
    # )

    driver.get(
        f"https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/{search_infos['brand']}/{search_infos['model']}/estado-df?f=p&me={search_infos['maxKm']}&ms={search_infos['minKm']}&re={search_infos['maxYear']}&rs={search_infos['minYear']}"
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
            car_price = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.hQZMji > div > div > div > div.ad__sc-en9h1n-0.IoqnP > div.ad__sc-1leoitd-2.fIICfM.olx-d-flex.olx-ai-flex-start.olx-fd-column > h2",
            ).text
            average_price = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.fnDpgM > div > div > div > div.sc-bcXHqe.sc-eDvSVe.caEdXs.hKQPaV > div:nth-child(1) > div.sc-bcXHqe.DqRAg > span",
            ).text
            fipe_price = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.fnDpgM > div > div > div > div.sc-bcXHqe.sc-eDvSVe.caEdXs.hKQPaV > div:nth-child(2) > div > span",
            ).text
            try:
                take_trades = driver.find_element(
                    By.CSS_SELECTOR,
                    "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.hdSEbB > div > div > div > div.olx-d-flex.olx-fd-column > div > div > span",
                ).text
            except NoSuchElementException:
                # If element not found, set take_trades to "Não aceita"
                take_trades = "Não aceita"
            car_year = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(5) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > a",
            ).text
            car_potency = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(7) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            car_km = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(6) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            car_shifter = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(10) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            car_steering_type = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(14) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            car_color = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(11) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            doors_number = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(12) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            gnv_kit = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ebdmHc > div > div > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div:nth-child(9) > div > div.olx-d-flex.olx-ml-2.olx-ai-baseline.olx-fd-column > span.olx-text.olx-text--body-medium.olx-text--block.olx-text--regular.olx-color-neutral-130",
            ).text
            announce_date = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.hRTDUb > div.ad__sc-h3us20-6.ckBKfA > div > div > div > span.olx-text.olx-text--caption.olx-text--block.olx-text--regular.ad__sc-1oq8jzc-0.dWayMW.olx-color-neutral-120",
            ).text
            announcer_name = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.dBnjzp > div.ad__sc-h3us20-6.bwBaLM > div > div > div > div.sc-gEvEer.sc-jnOGJG.fPFnoJ.bwWeeV > div.sc-gEvEer.sc-dZoequ.fPFnoJ.hVyURs > div.sc-gEvEer.sc-bBeLUv.fPFnoJ.ebacRy > div > div > div > div > span",
            ).text
            announcer_adress = driver.find_element(
                By.CSS_SELECTOR,
                "#content > div.ad__sc-18p038x-2.djeeke > div > div.sc-bwzfXH.ad__sc-h3us20-0.lbubah > div.ad__sc-duvuxf-0.ad__sc-h3us20-0.dBnjzp > div.ad__sc-h3us20-6.bwBaLM > div > div > div > div.sc-gEvEer.sc-jnOGJG.fPFnoJ.bwWeeV > div.sc-gEvEer.sc-dZoequ.fPFnoJ.hVyURs > div.sc-gEvEer.sc-eZkCL.fPFnoJ.miRdz > div:nth-child(1) > div > span.sc-eqUAAy.crJkyb.sc-ibQAlb.lUVuq",
            ).text

            time.sleep(3)

            driver.close()

            driver.switch_to.window(olx_main_tab)

            data_rows = []
            data = {
                "Nome": announcer_name,
                "Marca": search_infos["brand"],
                "Modelo": search_infos["model"],
                "Usuário Desde": user_since,
                "Preço": car_price,
                "Média de Preço": average_price,
                "Preço Tabela FIPE": fipe_price,
                "Aceita Trocas": take_trades,
                "Ano": car_year,
                "Potência": car_potency,
                "Quilometragem": car_km,
                "Câmbio": car_shifter,
                "Direção": car_steering_type,
                "Cor": car_color,
                "Portas": doors_number,
                "Kit GNV": gnv_kit,
                "Data do Anúncio": announce_date,
                "Endereço": announcer_adress,
                "Telefone": "teste",
            }
            data_rows.append(data)

            df_client_informations = pd.concat(
                [df_client_informations, pd.DataFrame(data_rows)]
            )
            print(df_client_informations)
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
