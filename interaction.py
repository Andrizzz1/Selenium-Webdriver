from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#Setup
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36")
chrome_options.add_experimental_option("detach",True)

driver =webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# articles = driver.find_element(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(articles.text)

first_name = driver.find_element(By.NAME, 'fName')
Last_name = driver.find_element(By.NAME, 'lName')
Email = driver.find_element(By.NAME, 'email')
button = driver.find_element(By.CLASS_NAME,'btn')
first_name.send_keys("Andrei")
Last_name.send_keys("Mandapat")
Email.send_keys("Andrei@gmail.com")

button.send_keys(Keys.ENTER)
# driver.quit()