import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# open a file to write links
filename = open("data.txt", "w")

chrome_driver_path = 'path/to/chromedriver'
driver = webdriver.Chrome()

url = 'https://paykoko.com/category?cattype=fashion'
driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait for the page to load

    # Calculate the new height and check if scrolling is needed
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Wait till the entire page to loaded
time.sleep(20)  # stop for 20 seconds
print("Waiting finished")

elements = driver.find_elements(
    By.CSS_SELECTOR, '.post-item.col-lg-3.col-md-4.col-sm-6')

for element in elements:
    a_tag = element.find_element(By.TAG_NAME, 'a')
    urlOfATag = a_tag.get_attribute('href')
    
    if urlOfATag != None:
        filename.write(f"{urlOfATag}\n")

driver.quit()
