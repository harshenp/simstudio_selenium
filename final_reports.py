from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from prices_store import prices,price_zyngBeanz,price_others
final_market_share_value = []

def final_reports(driver):
    wait = WebDriverWait(driver, 10)
    content = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[1]/div[1]/div[1]")))
    actual_content = content.text
    expected_content = "Did you hit your targets?"
    print(actual_content)
    if actual_content == expected_content:
        assert True
        print("Content is matched ")
    assert actual_content == expected_content, f"content verification failed. Expected: '{expected_content}', Actual: '{actual_content}'"

    # click on Expand all in Period-3
    exp_btn = driver.find_element(By.XPATH,"//button[@id='expand_all_report']")
    exp_btn.click()
    print("Expand all clicked")
    time.sleep(2)

    #table 1 (Profit and loss statement)
    print("* Tabel 1 (Profit and loss statement) *")
    #Month 1
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[2]/section/div/div[2]/table/tr[2]/td[5]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("month 1 : revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Month 2
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[2]/section/div/div[2]/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("month 2 : revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Month 3
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[2]/section/div/div[2]/table/tr[2]/td[3]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("month 3 : revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Month 4
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[2]/section/div/div[2]/table/tr[2]/td[2]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("month 4 : revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"



    #table2 
    print("* Tabel 2 (Cost structure) *")
    #month 1
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[3]/section/div/div/table/tr[2]/td[5]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("month 1 : revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"

    #month 2
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[3]/section/div/div/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("month 2 : revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #month 3
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[3]/section/div/div/table/tr[2]/td[3]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("month 3 : revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #month 4
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[2]/div[3]/section/div/div/table/tr[2]/td[2]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 100
    print(actual_revenue)
    if actual_revenue == expected_min_revenue:
        assert True
        print("month 4 : revenue Testing Passed")                                   
    assert actual_revenue == expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"



    # table 3  - Profit and Loss statement table (company wise)
    print("* Tabel 3 (Profit-loss company-wise) *")
    #ZyngBeanz
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[2]/section/div/div/table/tr[2]/td[2]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Alpha Corp.
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[2]/section/div/div/table/tr[2]/td[3]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"

    #Beta Group
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[2]/section/div/div/table/tr[2]/td[4]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Gamma Inc.
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[2]/section/div/div/table/tr[2]/td[5]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"
    #Delta Brothers
    revenue = driver.find_element(By.XPATH,"//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[2]/section/div/div/table/tr[2]/td[6]")
    actual_revenue = float(''.join(filter(str.isdigit, revenue.text)))
    expected_min_revenue = 0
    print(actual_revenue)
    if actual_revenue >= expected_min_revenue:
        assert True
        print("revenue Testing Passed")                                   
    assert actual_revenue >= expected_min_revenue, f"Revenue not matched . Expected: '{expected_min_revenue}', Actual: '{actual_revenue}'"

    #Table 4 Market Share Report (Unit Wise)
    print("*  Table 4 - Market Share Report (Unit Wise) * ")
    final_market_share = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[3]/section/div/div/table/tr[2]/td[2]").text.strip('%')
    final_market_share = float(final_market_share)
    final_market_share_value.append(final_market_share)

    print(final_market_share)

    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[3]/section/div/div/table")
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
        assert expected_range_min <= value <= expected_range_max,f'Error : Value {value} is outside the expected range. Expected: 0% to 50%, Actual: {value}'

    #Table 5 Market Share Report (Revenue Wise)
    print("* Table 5 - Market Share Report (Revenue Wise) *")
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[4]/section/div/div/table")
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
            assert True
            print(f'Value {value} is within the expected range (0% to 50%).')
        assert expected_range_min <= value <= expected_range_max,f'Error : Value {value} is outside the expected range. Expected: 0% to 50%, Actual: {value}'
    
    
    #Table 6 Market Report
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[2]/div[3]/div[5]/section/div/div/table")
    prices(table)
    
    #click next button
    next_btn = driver.find_element(By.XPATH,value="//*[@id='submit_user_input']")
    print("Next Button clicked")
    next_btn.click()
    time.sleep(5)