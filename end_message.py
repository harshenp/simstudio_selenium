from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time



def end_message(driver):  
    msg = driver.find_element(By.CLASS_NAME, 'sub_heading')
    actual_msg= msg.text
    expected_msg= "Congratulations on completing the simulation!\nHere are a few useful links for you."
    print(actual_msg)
    if actual_msg == expected_msg:
        assert True
        print("Text is matched ")
    assert actual_msg == expected_msg, f"Text verification failed. Expected: '{expected_msg}', Actual: '{actual_msg}'"

    play_btn = driver.find_element(By.XPATH,value="//*[@id='videos_container']/div/div[2]/span")
    print("clicked on Rewatch")
    play_btn.click()
    time.sleep(6)   

    close_btn = driver.find_element(By.XPATH,value="//*[@id='video_popup']/div/div/div/button")
    print("clicked on Video Close")
    close_btn.click()
    time.sleep(3)   
