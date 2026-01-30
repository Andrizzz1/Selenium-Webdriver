from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from datetime import datetime
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

# Wait up to 10 seconds for the element to be present
wait = WebDriverWait(driver, 10)
Language = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]')))
Language.click()

Auto_click = 0

timeout = time.time() + 5
while Auto_click < timeout:
    try:
        cookie = driver.find_element(By.ID,'bigCookie')
        cookie.click()
        
        cokkies = driver.find_element(By.ID,'cookies')
        total_Cookie = int(cokkies.text.split()[0])
        
        test = 0
        if test == 5 or time.time() > timeout:
            break
        test = test - 1
        print(test)
    except Exception as e:
        print(f"Error: {e}")
        continue
# driver.quit()  # Comment out if you want to see the result