from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Inicializando domínio ubisoft principal
driver.get("https://www.ubisoft.com/pt-br")

# Carregando cookies do arquivo
with open("ubi_cookies.pkl", "rb") as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        if 'sameSite' in cookie:
            del cookie['sameSite']
        driver.add_cookie(cookie)

# Inicializando página do marketplace r6 e recarregando-a
url = "https://www.ubisoft.com/pt-br/game/rainbow-six/siege/marketplace?route=buy%2Fitem-details&itemId=46c5cb0c-d095-4a10-82f8-c380dedd9aa4"
driver.get(url)
driver.refresh()

# Procurando avatar para verificação
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[class*="Topbar-image"]')))

try:
    # Procurando preço
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='price-tag-value']")))

    html_completo = driver.page_source
    soup = BeautifulSoup(html_completo, 'html.parser')
    preco_tag = soup.select_one("[data-testid='price-tag-value']")
    print("Preço do item" + preco_tag.text)

finally:
    print("Script finalizado")
    driver.quit()
