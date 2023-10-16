from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def end_content(driver):
    heading = driver.find_element(By.XPATH,value="//*[@id='content_video_page1']/div/div[1]")
    actual_heading = heading.text
    expected_heading = "An introduction to pricing"
    print(actual_heading)
    if actual_heading == expected_heading:
        assert True
        driver.save_screenshot('screenshots/assert_true/endcontent.png')
        print("Heading is matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/endcontent.png')    
    assert actual_heading == expected_heading, f"Heading verification failed. Expected: '{expected_heading}', Actual: '{actual_heading}'"


    play_btn = driver.find_element(By.XPATH,value="//*[@id='content_video_page1']/div/div[3]/div/i")
    print("clicked on Video Play")
    play_btn.click()
    time.sleep(6)   

    close_btn = driver.find_element(By.XPATH,value="//*[@id='video_popup']/div/div/div/button")
    print("clicked on Video Close")
    close_btn.click()
    time.sleep(3)   

    video_transcript = driver.find_element(By.XPATH,value="//*[@id='video_page1_transcript']").text
    expected_textlength = 1809 
    text_length = len(video_transcript)
    print(f"Length of text on the page: {text_length} characters")
    if text_length == expected_textlength:
        assert True
    assert text_length == expected_textlength,"Video Transcript Length mismatched"   

    next_btn = driver.find_element(By.XPATH,value="//*[@id='content_video_page1']/div/div[5]/button[2]")
    print("clicked on Next button ")
    next_btn.click()
    time.sleep(5)   
