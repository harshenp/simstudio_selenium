from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def market_deepdive(driver):
    heading = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-4']/div/div[3]")
    actual_heading = heading.text
    expected_heading = "Market Deep-dive"
    print(actual_heading)
    if actual_heading == expected_heading:
        assert True
        driver.save_screenshot('screenshots/assert_true/marketdeepdive.png')
        print("Heading is matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/marketdeepdive.png')   
    assert actual_heading == expected_heading, f"Heading verification failed. Expected: '{expected_heading}', Actual: '{actual_heading}'"

    text1 = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-4']/div/div[8]/div[1]")
    actual_text1= text1.text
    expected_text1 = "Final Market Share (Units)"
    print(actual_text1)
    if actual_text1 == expected_text1:
        driver.save_screenshot('screenshots/assert_true/marketdeepdive.png')
        assert True
        print("Text is matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/marketdeepdive.png')    
    assert actual_text1 == expected_text1, f"Text verification failed. Expected: '{expected_text1}', Actual: '{actual_text1}'"

    text2 = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-4']/div/div[9]/div[1]")
    actual_text2= text2.text
    expected_text2 = "Cumulative Operating Margin %"
    print(actual_text2)
    if actual_text2 == expected_text2:
        assert True
        driver.save_screenshot('screenshots/assert_true/marketdeepdive.png')
        print("Text is matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/marketdeepdive.png')    
    assert actual_text2 == expected_text2, f"Text verification failed. Expected: '{expected_text2}', Actual: '{actual_text2}'"

    #click on next
    next_btn = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-4']/div/div[2]/button[2]")
    print("clicked on Next button ")
    next_btn.click()
    time.sleep(5)   

