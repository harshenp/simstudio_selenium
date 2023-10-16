from selenium.webdriver.common.by import By
import time

def logout(driver):
    logout_btn = driver.find_element(By.XPATH,value="//*[@id='data_for_content_pages']/span")
    print("Logged out")
    logout_btn.click()
    time.sleep(3)   
