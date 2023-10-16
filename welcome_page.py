from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
    

def welcome_page(driver):
    ##checking simulation Name
    element = driver.find_element(By.XPATH,value="//div[@class='header-simulation-name padding-left-45 padding-top-10 padding-bottom-10 theme-font2']")
    actual_text = element.text
    expected_text = "Anchor"
    if actual_text == expected_text:
        assert True
        print("Simulation name is matched ")                                    
    assert actual_text == expected_text, f"Text verification failed. Expected: '{expected_text}', Actual: '{actual_text}'"

    #verify the heading
    heading = driver.find_element(By.XPATH,value="//div[@class='heading theme-font16']")
    actual_heading = heading.text
    expected_heading = "A new mission awaits!"
    print(actual_heading)
    if actual_heading == expected_heading:
        assert True
        print("Heading is matched ")
    assert actual_heading == expected_heading, f"Heading verification failed. Expected: '{expected_heading}', Actual: '{actual_heading}'"

    #verify the content
    content = driver.find_element(By.XPATH,value="//p[contains(text(),'As you open your laptop on a Monday morning, you h')]")
    actual_content = content.text
    expected_content = "As you open your laptop on a Monday morning, you have a mail from your Managing Director, Dr. Bean himself!"
    print(actual_content)
    if actual_content == expected_content:
        assert True
        print("Content is matched ")
    assert actual_content == expected_content, f"content verification failed. Expected: '{expected_content}', Actual: '{actual_content}'"

    content_intrigued = driver.find_element(By.XPATH,value="//p[contains(text(),'Intrigued, you open')]")
    actual_content_intrigued = content_intrigued.text
    expected_content_intregued = "Intrigued, you open the mail to see what it says…"
    print(actual_content_intrigued)
    if actual_content_intrigued == expected_content_intregued:
        assert True
        print("Content is matched ")
    assert actual_content_intrigued == expected_content_intregued, f"content verification failed. Expected: '{expected_content_intregued}', Actual: '{actual_content_intrigued}'"

