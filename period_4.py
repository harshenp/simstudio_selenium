from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from prices_store import prices

def period_4(driver):
    #market share (Month 4)
    time.sleep(2)
    market_share = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/span")
    actual_market_share = float(market_share.text.strip('%'))
    expected_min_market_share = 0
    expected_max_market_share =100
    print(market_share.text)
    if expected_min_market_share <= actual_market_share <= expected_max_market_share:
        assert True
        print("Market share is within the expected range")                                    
    assert expected_min_market_share <= actual_market_share <= expected_max_market_share, f"Text verification failed in Period 4. Expected:0% to 100% Actual: '{market_share.text}'"

    #Sliders
    extracted_values = []
    expected_values = {'147', '116692', '31284', '127001'}
    sliders = driver.find_elements(By.CSS_SELECTOR, '[role="slider"]')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[role="slider"]')))
    for slider in sliders:
        try:
            #slider = wait.until(EC.visibility_of(slider))
            aria_valuenow = slider.get_attribute('aria-valuenow')
            extracted_values.append(aria_valuenow)
        except Exception as e:
            print(f"Error while processing a slider: {e}")
    non_zero_values = [value for value in extracted_values if value != '0']
    non_zero_set = set(non_zero_values)
    if non_zero_set == expected_values:
        assert True
        print("Sliders values matched in period 4")
    assert non_zero_set == expected_values, f"Values do not match. Expected: {expected_values}, Actual: {non_zero_set}"

    proj_rev = driver.find_element(By.XPATH,"//div[@class='revenue_value theme-font8']")
    actual_proj_rev = float(''.join(filter(str.isdigit, proj_rev.text)))
    expected_min_proj_rev = 0
    print(actual_proj_rev)
    if actual_proj_rev >= expected_min_proj_rev:
        assert True
        print("Projected revenue Testing Passed in Period 4")                                    
    assert actual_proj_rev >= expected_min_proj_rev, f"Projected revenue not matched  . Expected: '{expected_min_proj_rev}', Actual: '{actual_proj_rev}'"

    # click on Expand all in Period-3
    exp_btn = driver.find_element(By.XPATH,"//button[@id='expand_all_report']")
    exp_btn.click()
    print("Expand all clicked")
    time.sleep(2)

    #table 1 (Profit and loss statement)
    print("* Tabel 1 (Profit and loss statement) *")
    #Month 1
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[2]/section/div/div[2]/table/tr[2]/td[5]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Month 2
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[2]/section/div/div[2]/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Month 3
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[2]/section/div/div[2]/table/tr[2]/td[3]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Month 4(E)
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[2]/section/div/div[2]/table/tr[2]/td[2]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"



    #table2 
    print("* Tabel 2 (Cost structure) *")
    #month 1
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"

    #month 2
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #month 3
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table/tr[2]/td[3]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #month 4(E)
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table/tr[2]/td[2]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"



    # table 3  - Profit and Loss statement table (company wise)
    print("* Tabel 3 (Profit-loss company-wise) *")
    #ZyngBeanz
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[2]/section/div/div/table/tr[2]/td[2]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Alpha Corp.
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[2]/section/div/div/table/tr[2]/td[3]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"

    #Beta Group
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[2]/section/div/div/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Gamma Inc.
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[2]/section/div/div/table/tr[2]/td[5]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Delta Brothers
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[2]/section/div/div/table/tr[2]/td[6]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"

    #Table 4 Market Share Report (Unit Wise)
    print("*  Table 4 - Market Share Report (Unit Wise) * ")
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[3]/section/div/div/table")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    market_share_values = table_data[0][1:]
    # Convert the percentage strings to floats and calculate the sum
    percentage_values = [float(value.strip('%')) for value in market_share_values]
    total_percentage = sum(percentage_values)
    tolerance = 1
    # Check if the total percentage equals 100%
    if abs(total_percentage - 100.0) <= tolerance:
        assert True
        print("Market Share values(Unit wise) add up to 100%")
    assert abs(total_percentage - 100.0) <= tolerance,f"Error : Market Share values(Unit wise) add up to {total_percentage}%"       


    expected_range_min = 0
    expected_range_max = 50

    # Extract and verify the values
    other_values = [float(value.strip('%')) for value in table_data[0][2:]] # Remaining columns for other companies (Leaving ZyngBeanz)

    # Check if the other company values are within the expected range
    for value in other_values:
        if expected_range_min <= value <= expected_range_max:
            assert True
            print(f'Value {value} is within the expected range (0% to 50%).')
        else:
            assert expected_range_min <= value <= expected_range_max,f'Error : Value {value} is outside the expected range. Expected: 0% to 50%, Actual: {value}'

    #Table 5 Market Share Report (Revenue Wise)
    print("* Table 5 - Market Share Report (Revenue Wise) *")
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[4]/section/div/div/table")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    market_share_values = table_data[0][1:]
    # Convert the percentage strings to floats and calculate the sum
    percentage_values = [float(value.strip('%')) for value in market_share_values]
    total_percentage = sum(percentage_values)
    tolerance = 1
    # Check if the total percentage equals 100%
    if abs(total_percentage - 100.0) <= tolerance:
        assert True
        print("Market Share values(Revenue wise) add up to 100%")
    assert abs(total_percentage - 100.0) <= tolerance,f"Error : Market Share values(Revenue wise) add up to {total_percentage}%"        

    expected_range_min = 0
    expected_range_max = 50

    # Extract and verify the values
    other_values = [float(value.strip('%')) for value in table_data[0][2:]] # Remaining columns for other companies (leaving zyngBeanz)

    # Check if the other company values are within the expected range
    for value in other_values:
        if expected_range_min <= value <= expected_range_max:
            print(f'Value {value} is within the expected range (0% to 50%).')
        else:
            assert expected_range_min <= value <= expected_range_max,f'Error : Value {value} is outside the expected range. Expected: 0% to 50%, Actual: {value}'


    #Table 6 Market Report
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[4]/div[5]/section/div/div/table")
    prices(table)

    ###Now manipulate the slider 
    
    #first slider-  Manipulate the slider value
    slider = driver.find_element(By.ID, "bucket-1-basic-slider1")
    pixels_to_move =130
    action_chains = ActionChains(driver)
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()
    time.sleep(1)
    #Second slider
    slider = driver.find_element(By.ID, "bucket-1-basic-slider2")
    pixels_to_move = -90
    action_chains = ActionChains(driver)
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()
    time.sleep(1)
    #3rd slider
    slider = driver.find_element(By.ID, "bucket-1-basic-slider3")
    pixels_to_move = -160
    action_chains = ActionChains(driver)
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()
    time.sleep(1)
    #4th slider
    slider = driver.find_element(By.ID, "bucket-1-basic-slider4")
    pixels_to_move = 90
    action_chains = ActionChains(driver)
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()
    time.sleep(1)

    ##click on submit button
    submit_btn = driver.find_element(By.XPATH,"//div[@id='submit_user_input']")
    submit_btn.click()
    print("Submit Button clicked")

    time.sleep(2)
    ##click yes on popup
    yes_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Yes']")
    yes_btn.click()
    print("Clicked yes button on popup meassage")

    time.sleep(6)
