from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def leaderboard(driver):
    print("* KPI 1 *")
    kpi_1 = driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-3']/div/div[5]/div[1]/div[2]")
    KPI_1_gettext = kpi_1.text
    expected_kpi_1 = "Final Market Share (Units)"
    print(KPI_1_gettext)
    assert KPI_1_gettext == expected_kpi_1, f"Text verification failed. Expected: '{expected_kpi_1}', Actual: '{KPI_1_gettext}'"


    table_body = driver.find_element(By.XPATH, "//*[@id='sib-de-brief-page-3']/div/div[5]/div[1]/table/tbody")
    rows = table_body.find_elements(By.TAG_NAME, 'tr')
    # Iterate through the rows to find "You"
    name_found = False
    for row in rows:
        name = row.find_elements(By.TAG_NAME, 'td')[1].text
        if 'You' in name:
            assert 'You' in name
            driver.save_screenshot('screenshots/assert_true/leaderboard.png')
            rank = row.find_elements(By.TAG_NAME, 'td')[0].text
            score = row.find_elements(By.TAG_NAME, 'td')[2].text
            name_found = True
            print(f"Name: {name}, Rank: {rank}, Score: {score}")
    if name_found == False:
        driver.save_screenshot('screenshots/assert_false/leaderboard.png')        
    assert name_found,"Something Wrong , Your name is not in leaderboard"

    print("* KPI 2 *")

    kpi_2 = driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-3']/div/div[5]/div[2]/div[2]")
    KPI_2_gettext = kpi_2.text
    expected_kpi_2 = "Cumulative Operating Margin %"
    print(KPI_2_gettext)
    assert KPI_2_gettext == expected_kpi_2, f"Text verification failed. Expected: '{expected_kpi_2}', Actual: '{KPI_2_gettext}'"


    table_body = driver.find_element(By.XPATH,"//*[@id='sib-de-brief-page-3']/div/div[5]/div[2]/table/tbody")
    rows = table_body.find_elements(By.TAG_NAME, 'tr')
    # Iterate through the rows to find "You"
    name_found = False
    for row in rows:
        name = row.find_elements(By.TAG_NAME, 'td')[1].text
        if 'You' in name:
            assert 'You' in name
            driver.save_screenshot('screenshots/assert_true/leaderboard.png')
            rank = row.find_elements(By.TAG_NAME, 'td')[0].text
            score = row.find_elements(By.TAG_NAME, 'td')[2].text
            name_found = True
            print(f"Name: {name}, Rank: {rank}, Score: {score}")
    if name_found == False:
        driver.save_screenshot('screenshots/assert_false/leaderboard.png')         
    assert name_found,"Something Wrong , Your name is not in leaderboard"


    #click on Market deep-dive
    fourth_btn = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-3']/div/div[2]/div[4]/div[1]")
    print("clicked on Market Deep-Dive ")
    fourth_btn.click()
    time.sleep(3)   
