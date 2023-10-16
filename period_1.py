from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def period_1(driver):
    ##verify sliders default values
    extracted_values = []
    expected_values = ['140', '100000', '50000', '100000']

    # Locate the sliders by using the 'role' attribute with the value 'slider'
    sliders = driver.find_elements(By.CSS_SELECTOR, '[role="slider"]')

    # Iterate through the sliders and extract 'aria-valuenow'
    for slider in sliders:
        try:
            aria_valuenow = slider.get_attribute('aria-valuenow')
            extracted_values.append(aria_valuenow)
        except Exception as e:
            # Handle any exceptions, e.g., when the attribute is not found
            print(f"Error while processing a slider: {e}")
    non_zero_values = [value for value in extracted_values if value != '0']
    if non_zero_values == expected_values:
        assert True
        print("Assertion passed. Values match the expected values.")
    assert non_zero_values == expected_values, f"Values do not match. Expected: {expected_values}, Actual: {non_zero_values}"

    #verify projected Revenue value

    proj_rev = driver.find_element(By.XPATH,"//div[@class='revenue_value theme-font8']")
    actual_proj_rev = proj_rev.text
    expected_proj_rev = "USD 1,142,400"
    if actual_proj_rev == expected_proj_rev:
        assert True
        print("Proj_rev is matched ")                               
    assert actual_proj_rev == expected_proj_rev, f"Text verification failed. Expected: '{expected_proj_rev}', Actual: '{actual_proj_rev}'"


    #verfy projected Operating margin

    proj_mg = driver.find_element(By.XPATH,"//div[@class='operating_margin_value theme-font8']")
    actual_proj_mg = proj_mg.text
    expected_proj_mg = "USD 57,720"
    if actual_proj_mg == expected_proj_mg:
        assert True
        print("Proj_mg is matched ")                            
    assert actual_proj_mg == expected_proj_mg, f"Text verification failed. Expected: '{expected_proj_mg}', Actual: '{actual_proj_mg}'"

    #company performance content
    perf_cont = driver.find_element(By.XPATH,"//div[@class='theme-font7 font-weight-500 padding-top-10']")
    actual_perf_cont = perf_cont.text
    expected_perf_cont = "Performance is calculated considering similar market share as last month: 20%"
    if actual_perf_cont == expected_perf_cont:
        assert True
        print("perf_cont is matched ")                              
    assert actual_perf_cont == expected_perf_cont, f"Text verification failed. Expected: '{expected_perf_cont}', Actual: '{actual_perf_cont}'"

    #click on expand all
    exp_btn = driver.find_element(By.XPATH,"//button[@id='expand_all_report']")
    exp_btn.click()
    print("Expand all clicked")

    time.sleep(2)
    #Profit And Loss Statement
    pl_cont = driver.find_element(By.XPATH,"//div[@class='theme-font7 font-weight-500']")
    print(pl_cont.text)
    actual_pl_cont = pl_cont.text
    expected_pl_cont = "Hover over the items for the explanation."
    if actual_pl_cont == expected_pl_cont:
        assert True
        print("profit loss statement matched")                             
    assert actual_pl_cont == expected_pl_cont, f"Text verification failed. Expected: '{expected_pl_cont}', Actual: '{actual_pl_cont}'"


    ##verify profit-loss table default data
    table = driver.find_element(By.CLASS_NAME, "bold_pandl")

    # Extract data from the table
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    # Define the expected data
    expected_data = [
        ["Revenue", "1,142,400"],
        ["COGS", "(799,680)"],
        ["Gross Margin", "342,720"],
        ["Fixed Cost", "(23,000)"],
        ["Advertising", "(100,000)"],
        ["Sales Force Cost", "(50,000)"],
        ["Quality Control Cost", "(100,000)"],
        ["Admin Expense", "(12,000)"],
        ["Operating Margin / EBITDA", "57,720"]
    ]
    if table_data == expected_data:
        assert True
        print("Default pl table data matched" )
    assert table_data == expected_data, "Profit-Loss Table default content does not match the expected data"


    ##verify cost structure table default data
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table")

    # Extract data from the table
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    # Define the expected data
    expected_data = [
        ["Revenue", "100%"],
        ["COGS", "(70)%"],
        ["Gross Margin", "30%"],
        ["Fixed Cost", "(2)%"],
        ["Advertising", "(9)%"],
        ["Sales Force Cost", "(4)%"],
        ["Quality Control Cost", "(9)%"],
        ["Admin Expense", "(1)%"],
        ["Operating Margin / EBITDA", "5%"]
    ]
    if table_data == expected_data:
        assert True
        print("Default Cost Structure table data matched" )
    assert table_data == expected_data, " Cost Structure Table Default content does not match the expected data"


    #### Heading - Now we are checking all the things on manipulation 
    #first slider-  Manipulate the slider value
    slider = driver.find_element(By.ID, "bucket-1-basic-slider1")

    slider_width = slider.size["width"]

    # Get the current value of the slider
    current_value = int(slider.get_attribute("aria-valuenow"))

    # Calculate the new position based on the desired value 
    desired_value = 145
    temp_value = desired_value+1
    position_change = temp_value - current_value
    new_position = (position_change / (160 - 120)) * slider_width

    # Use ActionChains to move the slider to the new position
    action_chains = ActionChains(driver)
    action_chains.click_and_hold(slider).move_by_offset(new_position, 0).release().perform()

    # Verify the updated value
    updated_value = slider.get_attribute("aria-valuenow")
    print(f"Updated value: {updated_value}")
    updated_value = type(desired_value)(updated_value)
    assert updated_value==desired_value,f"Could not move as desired . Expected: '{desired_value}', Actual: '{updated_value}'"
    time.sleep(1)


    #now check changes on projected revenue and projected margin after first slider regulation
    proj_rev = driver.find_element(By.XPATH,"//div[@class='revenue_value theme-font8']")
    actual_proj_rev = proj_rev.text
    expected_proj_rev = "USD 1,183,200"
    print(actual_proj_rev)
    if actual_proj_rev == expected_proj_rev:
        assert True
        print("Proj_rev is matched after first manipulation")                            
    assert actual_proj_rev == expected_proj_rev, f"Text verification failed in first slider regulation. Expected: '{expected_proj_rev}', Actual: '{actual_proj_rev}'"

    proj_mg = driver.find_element(By.XPATH,"//div[@class='operating_margin_value theme-font8']")
    actual_proj_mg = proj_mg.text
    expected_proj_mg = "USD 98,520"
    print(actual_proj_mg)
    if actual_proj_mg == expected_proj_mg:
        assert True
        print("Proj_mg is matched after first manipulation ")                                   
    assert actual_proj_mg == expected_proj_mg, f"Text verification failed in first slider regulation. Expected: '{expected_proj_mg}', Actual: '{actual_proj_mg}'"

    #now check changes on tables after first slider regulation
    #table 1
    table = driver.find_element(By.CLASS_NAME, "bold_pandl")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "1,183,200"],
        ["COGS", "(799,680)"],
        ["Gross Margin", "383,520"],
        ["Fixed Cost", "(23,000)"],
        ["Advertising", "(100,000)"],
        ["Sales Force Cost", "(50,000)"],
        ["Quality Control Cost", "(100,000)"],
        ["Admin Expense", "(12,000)"],
        ["Operating Margin / EBITDA", "98,520"]
    ]
    if table_data == expected_data:
        assert True
        print("pl table data matched after first slider manipulation" )
    assert table_data == expected_data, " After first slider manipulation Profit-Loss Table content does not match the expected data"

    #table2 
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "100%"],
        ["COGS", "(68)%"],
        ["Gross Margin", "32%"],
        ["Fixed Cost", "(2)%"],
        ["Advertising", "(8)%"],
        ["Sales Force Cost", "(4)%"],
        ["Quality Control Cost", "(8)%"],
        ["Admin Expense", "(1)%"],
        ["Operating Margin / EBITDA", "8%"]
    ]
    if table_data == expected_data:
        assert True
        print("Cost Structure table data matched after first silder manipulation" )
    assert table_data == expected_data, " After first slider manipulation Cost Structure Table content does not match the expected data"

    ##Second  slider-  Manipulation

    slider = driver.find_element(By.ID, "bucket-1-basic-slider2")
    pixels_to_move = 150

    # Create an ActionChains object
    action_chains = ActionChains(driver)

    # Click and hold the slider's thumb, move it by the specified pixels, and then release it
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()

    time.sleep(1)


    #now check changes on projected revenue and projected margin second  slider regulation
    proj_rev = driver.find_element(By.XPATH,"//div[@class='revenue_value theme-font8']")
    actual_proj_rev = proj_rev.text
    expected_proj_rev = "USD 1,183,200"
    print(actual_proj_rev)
    if actual_proj_rev == expected_proj_rev:
        assert True
        print("Proj_rev is matched after second manipulation")                                
    assert actual_proj_rev == expected_proj_rev, f"Text verification failed in second slider regulation. Expected: '{expected_proj_rev}', Actual: '{actual_proj_rev}'"

    proj_mg = driver.find_element(By.XPATH,"//div[@class='operating_margin_value theme-font8']")
    actual_proj_mg = proj_mg.text
    expected_proj_mg = "USD 61,210"
    print(actual_proj_mg)
    if actual_proj_mg == expected_proj_mg:
        assert True
        print("Proj_mg is matched after second manipulation ")                                  
    assert actual_proj_mg == expected_proj_mg, f"Text verification failed in second slider regulation. Expected: '{expected_proj_mg}', Actual: '{actual_proj_mg}'"

    #now check changes on tables after Second slider regulation
    #table 1
    table = driver.find_element(By.CLASS_NAME, "bold_pandl")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "1,183,200"],
        ["COGS", "(799,680)"],
        ["Gross Margin", "383,520"],
        ["Fixed Cost", "(23,000)"],
        ["Advertising", "(137,310)"],
        ["Sales Force Cost", "(50,000)"],
        ["Quality Control Cost", "(100,000)"],
        ["Admin Expense", "(12,000)"],
        ["Operating Margin / EBITDA", "61,210"]
    ]
    if table_data == expected_data:
        assert True
        print("pl table data matched after second slider manipulation" )
    assert table_data == expected_data, " After second slider manipulation Profit-Loss Table content does not match the expected data"

    #table2 
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "100%"],
        ["COGS", "(68)%"],
        ["Gross Margin", "32%"],
        ["Fixed Cost", "(2)%"],
        ["Advertising", "(12)%"],
        ["Sales Force Cost", "(4)%"],
        ["Quality Control Cost", "(8)%"],
        ["Admin Expense", "(1)%"],
        ["Operating Margin / EBITDA", "5%"]
    ]
    if table_data == expected_data:
        assert True
        print("Cost Structure table data matched after second silder manipulation" )
    assert table_data == expected_data, " After second slider manipulation Cost Structure Table content does not match the expected data"




    ##3rd slider-  Manipulation

    slider = driver.find_element(By.ID, "bucket-1-basic-slider3")
    pixels_to_move = -150

    # Create an ActionChains object
    action_chains = ActionChains(driver)

    # Click and hold the slider's thumb, move it by the specified pixels, and then release it
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()

    time.sleep(1)


    #now check changes on projected revenue and projected margin 3rd  slider regulation
    proj_rev = driver.find_element(By.XPATH,"//div[@class='revenue_value theme-font8']")
    actual_proj_rev = proj_rev.text
    expected_proj_rev = "USD 1,183,200"
    print(actual_proj_rev)
    if actual_proj_rev == expected_proj_rev:
        assert True
        print("Proj_rev is matched after 3rd manipulation")                                    
    assert actual_proj_rev == expected_proj_rev, f"Text verification failed in 3rd slider regulation. Expected: '{expected_proj_rev}', Actual: '{actual_proj_rev}'"

    proj_mg = driver.find_element(By.XPATH,"//div[@class='operating_margin_value theme-font8']")
    actual_proj_mg = proj_mg.text
    expected_proj_mg = "USD 81,215"
    print(actual_proj_mg)
    if actual_proj_mg == expected_proj_mg:
        assert True
        print("Proj_mg is matched after 3rd manipulation ")                                     
    assert actual_proj_mg == expected_proj_mg, f"Text verification failed in 3rd slider regulation. Expected: '{expected_proj_mg}', Actual: '{actual_proj_mg}'"

    #now check changes on tables after 3rd slider regulation
    #table 1
    table = driver.find_element(By.CLASS_NAME, "bold_pandl")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "1,183,200"],
        ["COGS", "(799,680)"],
        ["Gross Margin", "383,520"],
        ["Fixed Cost", "(23,000)"],
        ["Advertising", "(137,310)"],
        ["Sales Force Cost", "(29,995)"],
        ["Quality Control Cost", "(100,000)"],
        ["Admin Expense", "(12,000)"],
        ["Operating Margin / EBITDA", "81,215"]
    ]
    if table_data == expected_data:
        assert True
        print("pl table data matched after 3rd slider manipulation" )
    assert table_data == expected_data, " After 3rd slider manipulation Profit-Loss Table content does not match the expected data"

    #table2 
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "100%"],
        ["COGS", "(68)%"],
        ["Gross Margin", "32%"],
        ["Fixed Cost", "(2)%"],
        ["Advertising", "(12)%"],
        ["Sales Force Cost", "(3)%"],
        ["Quality Control Cost", "(8)%"],
        ["Admin Expense", "(1)%"],
        ["Operating Margin / EBITDA", "7%"]
    ]
    if table_data == expected_data:
        assert True
        print("Cost Structure table data matched after 3rd silder manipulation" )
    assert table_data == expected_data, " After 3rd slider manipulation Cost Structure Table content does not match the expected data"

    ##4th slider-  Manipulation

    slider = driver.find_element(By.ID, "bucket-1-basic-slider4")
    pixels_to_move = 200

    action_chains = ActionChains(driver)
    action_chains.click_and_hold(slider).move_by_offset(pixels_to_move, 0).release().perform()

    time.sleep(1)


    #now check changes on projected revenue and projected margin 4th  slider regulation
    proj_rev = driver.find_element(By.XPATH,"//div[@class='revenue_value theme-font8']")
    actual_proj_rev = proj_rev.text
    expected_proj_rev = "USD 1,183,200"
    print(actual_proj_rev)
    if actual_proj_rev == expected_proj_rev:
        assert True
        print("Proj_rev is matched after 4th manipulation")
    else:                                     
        assert False, f"Text verification failed in 4th slider regulation. Expected: '{expected_proj_rev}', Actual: '{actual_proj_rev}'"

    proj_mg = driver.find_element(By.XPATH,"//div[@class='operating_margin_value theme-font8']")
    actual_proj_mg = proj_mg.text
    expected_proj_mg = "USD 31,018"
    print(actual_proj_mg)
    if actual_proj_mg == expected_proj_mg:
        assert True
        print("Proj_mg is matched after 4th manipulation ")
    assert actual_proj_mg == expected_proj_mg, f"Text verification failed in 4th slider regulation. Expected: '{expected_proj_mg}', Actual: '{actual_proj_mg}'"

    #now check changes on tables after 4th slider regulation
    #table 1
    table = driver.find_element(By.CLASS_NAME, "bold_pandl")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "1,183,200"],
        ["COGS", "(799,680)"],
        ["Gross Margin", "383,520"],
        ["Fixed Cost", "(23,000)"],
        ["Advertising", "(137,310)"],
        ["Sales Force Cost", "(29,995)"],
        ["Quality Control Cost", "(150,197)"],
        ["Admin Expense", "(12,000)"],
        ["Operating Margin / EBITDA", "31,018"]
    ]
    if table_data == expected_data:
        assert True
        print("pl table data matched after 4th slider manipulation" )
    assert table_data == expected_data, " After 4th slider manipulation Profit-Loss Table content does not match the expected data"

    #table2 
    table = driver.find_element(By.XPATH, "//*[@id='sib_gametype_container']/div/div/div[3]/div[3]/div/div/div[3]/div[3]/section/div/div/table")
    table_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        if row_data:
            table_data.append(row_data)

    expected_data = [
        ["Revenue", "100%"],
        ["COGS", "(68)%"],
        ["Gross Margin", "32%"],
        ["Fixed Cost", "(2)%"],
        ["Advertising", "(12)%"],
        ["Sales Force Cost", "(3)%"],
        ["Quality Control Cost", "(13)%"],
        ["Admin Expense", "(1)%"],
        ["Operating Margin / EBITDA", "3%"]
    ]
    if table_data == expected_data:
        assert True
        print("Cost Structure table data matched after 4th silder manipulation" )
    assert table_data == expected_data, " After 4th slider manipulation Cost Structure Table content does not match the expected data"

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

    time.sleep(2)
    ##click ok on 2nd popup
    ok_btn = driver.find_element(By.XPATH,"//button[normalize-space()='OK']")
    ok_btn.click()
    print("Clicked ok button on 2nd popup")
    time.sleep(3)