from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys 
import time
import threading

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
Auto_click = True


def parse_cookie_number(text):
    """Convert Cookie Clicker number format to integer"""
    text = text.strip().lower()
    
    if not text or text == '':
        return 0
    
    # Remove commas
    text = text.replace(',', '')
    
    # Handle million, billion, trillion, etc.
    multipliers = {
        'million': 1_000_000,
        'billion': 1_000_000_000,
        'trillion': 1_000_000_000_000,
        'quadrillion': 1_000_000_000_000_000,
    }
    
    for word, multiplier in multipliers.items():
        if word in text:
            # Extract the number part (e.g., "1.4" from "1.4 million")
            number = float(text.replace(word, '').strip())
            return int(number * multiplier)
    
    # If no special format, just convert to int
    try:
        return int(float(text))
    except:
        return 0
    
def fiveSec_Timer():
    global Auto_click
    
    while True:
        time.sleep(5) #wait 5 seconds
        Auto_click = False
        try:

            driver.current_url # This will throw error if session is dead
            #for cookies count
            cookies_text = driver.find_element(By.ID,"cookies").text.split()[0].replace(',','')
            if not cookies_text:
                Auto_click = True
                continue
            
            cookies_total = parse_cookie_number(cookies_text)
            #Elements
            Curser_element = driver.find_element(By.ID,"product0")
            Grandma_element = driver.find_element(By.ID,"product1")
            Farm_element = driver.find_element(By.ID,"product2")
            Mine_element = driver.find_element(By.ID,"product3")
            Factory_element = driver.find_element(By.ID,"product4")
            Bank_element = driver.find_element(By.ID,"product5")
            Temple_element = driver.find_element(By.ID,"product6")
            WizardTower_element = driver.find_element(By.ID,"product7")
            Shipment_element = driver.find_element(By.ID,"product8")

            #Prices
            Curser = parse_cookie_number(driver.find_element(By.ID,"productPrice0").text)
            Grandma = parse_cookie_number(driver.find_element(By.ID,"productPrice1").text)
            Farm = parse_cookie_number(driver.find_element(By.ID,"productPrice2").text)
            Mine = parse_cookie_number(driver.find_element(By.ID,"productPrice3").text)
            Factory = parse_cookie_number(driver.find_element(By.ID,"productPrice4").text)
            Bank = parse_cookie_number(driver.find_element(By.ID,"productPrice5").text)
            Temple = parse_cookie_number(driver.find_element(By.ID,"productPrice6").text)
            WizardTower = parse_cookie_number(driver.find_element(By.ID,"productPrice7").text)
            Shipment = parse_cookie_number(driver.find_element(By.ID,"productPrice8").text)
            

            if Shipment and (cookies_total) >= Shipment:
                Shipment_element.click()
            elif WizardTower and cookies_total >= WizardTower:
                WizardTower_element.click()
            elif Temple and cookies_total >= Temple:
                Temple_element.click()
            elif Bank and cookies_total >= Bank:
                Bank_element.click()
            elif Factory and cookies_total >= Factory:
                Factory_element.click()
            elif Mine and cookies_total >=Mine:
                Mine_element.click()
            elif Farm and cookies_total >= Farm:
                Farm_element.click()
            elif Grandma and cookies_total >= Grandma:
                Grandma_element.click()
            elif Curser and cookies_total >= Curser:
                Curser_element.click()


            

        except Exception as e:
            print(f"Error: {e}")
        

        Auto_click = True



# Start the timer in a separate thread
timer_thread = threading.Thread(target=fiveSec_Timer)
timer_thread.start()


bigCookie = driver.find_element(By.ID,'bigCookie')
while True:
    if Auto_click:
        bigCookie.click()


# driver.quit()  # Comment out if you want to see the result