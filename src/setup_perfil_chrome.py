import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

chrome_profile_path = "./chrome-profile"

options = Options()
options.add_argument(f"user-data-dir={chrome_profile_path}")
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["pt-BR", "pt"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.ubisoft.com/pt-br/game/rainbow-six/siege/marketplace"
driver.get(url)
time.sleep(300)
driver.quit()