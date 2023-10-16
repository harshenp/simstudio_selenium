from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def your_performance(driver):
    heading = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-2']/div/div[3]")
    actual_heading = heading.text
    expected_heading = "Your Performance"
    print(actual_heading)
    if actual_heading == expected_heading:
        assert True
        driver.save_screenshot('screenshots/assert_true/yourperformance.png')
        print("Heading is matched ")
    assert actual_heading == expected_heading, f"Heading verification failed. Expected: '{expected_heading}', Actual: '{actual_heading}'"

    #click on Leaderboard
    third_btn = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-2']/div/div[2]/div[3]/div[1]")
    print("clicked on your Leaderboard ")
    third_btn.click()
    time.sleep(3)   