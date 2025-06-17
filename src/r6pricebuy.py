from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_profile_path = "/.chrome-profile"

options = Options()
options.add_argument(f"user-data-dir={chrome_profile_path}")

driver = webdriver.Chrome(options=options)

try:
    url_item = "https://www.ubisoft.com/pt-br/game/rainbow-six/siege/marketplace?route=buy%2Fitem-details&itemId=8b9b75a2-4ed6-49aa-a403-a1f4122c75c6"
    driver.get(url_item)

    seletor_do_preco = '[data-testid="price-tag-value"]'
    
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, seletor_do_preco)))

    html_completo = driver.page_source
    soup = BeautifulSoup(html_completo, 'html.parser')
    preco_tag = soup.select_one(seletor_do_preco)

    if preco_tag:
        print(f"Sucesso! preço encontrado: {preco_tag.get_text(strip=True)}")
    else:
        print('Preço não encontrado')

finally:
    driver.quit()
