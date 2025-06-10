import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get("https://account.ubisoft.com/pt-BR/login")

try:
    timeout = 300
    elemento_confirmacao = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[class*="Topbar-image"]')))

    print("Login realizado")

    print("Navegando para página do marketplace para receber cookies finais.")
    driver.get("https://www.ubisoft.com/pt-br/game/rainbow-six/siege/marketplace")

    time.sleep(10)
    print("Página marketplace carregada com sucesso")

    with open("ubi_cookies.pkl", "wb") as file:
        pickle.dump(driver.get_cookies(), file)

    print("Cookies salvos")

except TimeoutException:
    print("Login não detectado no tempo estipulado. Script encerrando...")

finally:
    driver.quit()