from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from prices_store import price_zyngBeanz,price_others
from final_reports import final_market_share_value

def target_vs_actual(driver):
    #verify header
    heading = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[3]")
    actual_heading = heading.text
    expected_heading = "Target vs Actual"
    print(actual_heading)
    if actual_heading == expected_heading:
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
        print("Heading is matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')   
    assert actual_heading == expected_heading, f"Heading verification failed. Expected: '{expected_heading}', Actual: '{actual_heading}'"

    ###Avg prices
    your_avg_price_element = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[1]/div[3]/div[1]").text
    your_avg_price = your_avg_price_element.split('USD')[1].strip()
    your_avg_price = int(your_avg_price)
    int_values_zyngBeanz = [int(value) for value in price_zyngBeanz]
    total_price_zyngBeanz = sum(int_values_zyngBeanz)
    zyngbeanz_avg_price = round(total_price_zyngBeanz/4)
    if your_avg_price == zyngbeanz_avg_price:
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
        print("Your Avg price matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert your_avg_price == zyngbeanz_avg_price,"Your avg prices are not matched"  



    others_avg_price_element = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[1]/div[3]/div[2]").text
    others_avg_price = others_avg_price_element.split('USD')[1].strip()
    others_avg_price = int(others_avg_price)
    int_value_others = [int(value) for value in price_others]
    total_price_others = sum(int_value_others)
    other_comp_avg_price = round(total_price_others/16)
    if others_avg_price == other_comp_avg_price:
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
        print("Others Avg price matched ")
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert others_avg_price == other_comp_avg_price,"Others avg prices are not matched"  

    expected_final_missed_message = "You missed the target. Use this as a learning & show better results next time."
    expected_final_exceeded_message = "Congratulations, you nailed it! Mission accomplished, great job!"
    real_final_message = driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[6]").text
    expected_target_kpi1 = 27
    expected_target_kpi2 = 5



    # #verify Kpi1 and kpi2 
    Target_kpi1 =driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[2]/div[4]/div[1]").text.strip('%')
    Target_kpi1 = float(Target_kpi1)
    if Target_kpi1 == expected_target_kpi1:
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert Target_kpi1 == expected_target_kpi1,"Target dismatched"

    achieved_kpi1 =driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[2]/div[4]/div[2]").text.strip("%")
    achieved_kpi1 = float(achieved_kpi1)
    print(final_market_share_value[0])
    print(achieved_kpi1)
    if achieved_kpi1 == final_market_share_value[0]:
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert achieved_kpi1 == final_market_share_value[0],"Achieved dismatched"

    difference_in_kpi1 =driver.find_element(by=By.XPATH,value="//div[contains(@class,'child2')]//div[@class='col-6 heading2 theme-font2']").text.split('%')[0]
    print(difference_in_kpi1)
    difference_in_kpi1 = float(difference_in_kpi1)
    print(difference_in_kpi1)
    print(abs(Target_kpi1-achieved_kpi1))
    if difference_in_kpi1 == abs(Target_kpi1-achieved_kpi1):
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert difference_in_kpi1 == abs(Target_kpi1-achieved_kpi1),"Difference dismatched"


    Target_kpi2 =driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[3]/div[4]/div[1]").text.strip('%')
    Target_kpi2 = float(Target_kpi2)

    if Target_kpi2 == expected_target_kpi2:
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert Target_kpi2 == expected_target_kpi2,"Target dismatched"

    achieved_kpi2 =driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[3]/div[4]/div[2]").text.strip('%')
    achieved_kpi2 = float(achieved_kpi2)


    difference_in_kpi2 =driver.find_element(by=By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[5]/div[3]/div[2]/div[2]").text.split('%')[0]
    difference_in_kpi2 = float(difference_in_kpi2)

    if difference_in_kpi2 == abs(Target_kpi2 - achieved_kpi2):
        assert True
        driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
    else:
        driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
    assert difference_in_kpi2 == abs(Target_kpi2-achieved_kpi2),"Difference dismatched"



    kpi_1 = driver.find_element(by=By.XPATH,value="//body/div[1]/div[2]/div[1]/div[5]/div[2]/div[2]/div[2]/span[1]")
    KPI_1_gettext = kpi_1.text
    print(f"KPI 1 : {KPI_1_gettext}")
    kpi_2 = driver.find_element(by=By.XPATH,value="//body/div[1]/div[2]/div[1]/div[5]/div[3]/div[2]/div[2]/span[1]")
    KPI_2_gettext = kpi_2.text
    print(f"KPI 2 : {KPI_2_gettext}")

    if KPI_1_gettext != KPI_2_gettext:
        if real_final_message == expected_final_missed_message:
            assert True
            driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
        else:
            driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
        assert real_final_message == expected_final_missed_message, "message mismatched"

    elif KPI_1_gettext == KPI_2_gettext == 'Missed':
        if real_final_message == expected_final_missed_message:
            assert True
            driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
        else:
            driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
        assert real_final_message == expected_final_missed_message, "message mismatched"

    elif KPI_1_gettext == KPI_2_gettext == 'Exceeded':
        if real_final_message == expected_final_exceeded_message:
            assert True
            driver.save_screenshot('screenshots/assert_true/targetVSactual.png')
        else:
            driver.save_screenshot('screenshots/assert_false/targetVSactual.png')     
        assert real_final_message == expected_final_exceeded_message, "message mismatched"

    else:
        assert False, "something wrong"


    #click on your performance 
    second_btn = driver.find_element(By.XPATH,value="//*[@id='sib-de-brief-page-1']/div/div[2]/div[2]/div[1]")
    print("clicked on your performance ")
    second_btn.click()
    time.sleep(3)   
