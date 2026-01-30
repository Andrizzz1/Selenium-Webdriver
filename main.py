from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #to be trusted by the website


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)


# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")


# price = driver.find_element(By.CLASS_NAME,"a-price-whole")
# price_decimal = driver.find_element(By.CLASS_NAME,"a-price-fraction")

# whole_price=f"{price.text}.{price_decimal.text}"
# print(whole_price)


Events = {}
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR,".event-widget .shrubbery .menu time")
names = driver.find_elements(By.CSS_SELECTOR,".event-widget .shrubbery .menu a")



for date,value in enumerate(dates):  
    key = str(date)
    values= {'text':value.text}
    Events[key] = values


for i, name in enumerate(names):
    index = str(i)
    name_val = {'name':name.text}
    Events[index].update(name_val)
print(Events)
driver.quit()

