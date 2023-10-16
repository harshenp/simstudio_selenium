from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decimal import Decimal
from case_summary import case_summary
from period_1 import period_1
from period_2 import period_2
from period_3 import period_3
from period_4 import period_4
from final_reports import final_reports
from target_vs_actual import target_vs_actual
from your_performance import your_performance
from leaderboard import leaderboard
from market_deepdive import market_deepdive
from end_content import end_content
from end_message import end_message
from logout_btn import logout
from welcome_page import welcome_page



option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.maximize_window()

url = "https://simstudio-uat.catalyx.live/signin?module_id=d37817a3-a0c8-4942-a788-c000af6265e0"
username = "64@gmail.com"


driver.get(url)
time.sleep(3)

#login 
login = driver.find_element(By.XPATH, value="//input[@id='user_name']")
login.send_keys(username,Keys.ENTER)
print("Login Test Pass")
time.sleep(7)

#welcome page
welcome_page(driver)

#click next 
def click_next_button(driver, button_xpath):
    
    button = driver.find_element(By.XPATH,value=button_xpath)
    button.click()
    print("Next button clicked")
    
for click in range(3):
    click = click_next_button(driver,"//button[@class='nextButton theme-font15']")
    time.sleep(5)


# #case summary page content
print("* Case summary *")
case_summary(driver)

print("************* Testing in Period 1 ************** ")
period_1(driver)

## Period 2 

print("************* Testing in Period 2 ************** ")
period_2(driver)

## Period 3 

print("************* Testing in Period 3 ************** ")
period_3(driver)

### Period 4

print("************* Testing in Period 4 ************** ")
period_4(driver)

print("************* Testing After Submit all periods ************** ")
final_reports(driver)

##### De-brief 
print("************* Target vs Actual ************** ")
target_vs_actual(driver)


print("************* Your Performance ************** ")
your_performance(driver)


print("************* Leaderboard ************** ")
leaderboard(driver)

print("************* Market Deep-dive ************** ")
market_deepdive(driver)

print("************* Ending Page  ************** ")
end_content(driver)

print("************* End Message  ************** ")
end_message(driver)

full_screen = driver.find_element(By.XPATH,value="//*[@id='header_full_screen_icon']")
print("clicked on Full Screen")
full_screen.click()
time.sleep(3)   

#logout
logout(driver)

print("URL : https://simstudio-uat.catalyx.live/signin?module_id=d37817a3-a0c8-4942-a788-c000af6265e0")