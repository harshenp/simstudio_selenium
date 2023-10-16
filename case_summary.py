from selenium.webdriver.common.by import By
import time

def case_summary(driver):
    kpi_1_content = driver.find_element(By.XPATH,value="//div[normalize-space()='Final Market Share (Units)']")
    actual_kpi_1_content = kpi_1_content.text
    expected_kpi_1_content = "Final Market Share (Units)"
    print(actual_kpi_1_content)
    if actual_kpi_1_content == expected_kpi_1_content:
        print("kpi Content is matched ")
        assert True
    assert actual_kpi_1_content == expected_kpi_1_content, f"content verification failed. Expected: '{expected_kpi_1_content}', Actual: '{actual_kpi_1_content}'"


    kpi_1_perc = driver.find_element(By.XPATH,value="//div[@class='case_study_container']//div[1]//div[4]")
    actual_kpi_1_perc = kpi_1_perc.text
    expected_kpi_1_perc = "27 %"
    print(actual_kpi_1_perc)
    if actual_kpi_1_perc == expected_kpi_1_perc:
        assert True
        print("kpi_perc Content is matched ")
    assert actual_kpi_1_perc == expected_kpi_1_perc, f"content verification failed. Expected: '{expected_kpi_1_perc}', Actual: '{actual_kpi_1_perc}'"


    kpi_2_content = driver.find_element(By.XPATH,value="//div[normalize-space()='Cumulative Operating Margin %']")
    actual_kpi_2_content = kpi_2_content.text
    expected_kpi_2_content = "Cumulative Operating Margin %"
    print(actual_kpi_2_content)
    if actual_kpi_2_content == expected_kpi_2_content:
        assert True
        print("kpi Content is matched ")
    assert actual_kpi_2_content == expected_kpi_2_content, f"content verification failed. Expected: '{expected_kpi_2_content}', Actual: '{actual_kpi_2_content}'"


    kpi_2_perc = driver.find_element(By.XPATH,value="//div[@id='sib_case_study']//div[2]//div[4]")
    actual_kpi_2_perc = kpi_2_perc.text
    expected_kpi_2_perc = "5 %"
    print(actual_kpi_2_perc)
    if actual_kpi_2_perc == expected_kpi_2_perc:
        assert True
        print("kpi_perc Content is matched ")
    assert actual_kpi_2_perc == expected_kpi_2_perc, f"content verification failed. Expected: '{expected_kpi_2_perc}', Actual: '{actual_kpi_2_perc}'"

    #verify 1st table content
    table1 = driver.find_element(By.XPATH,value="//*[@id='sib_case_study']/div/div[6]/div[1]/table")

    # Get all the rows of the table except for the first row (heading row)
    rows_table1 = table1.find_elements(By.XPATH,value="//*[@id='sib_case_study']/div/div[6]/div[1]/table/tbody/tr")

    # Initialize a list to store the table data
    table1_data = []

    # Iterate through the rows and extract cell data
    for row in rows_table1:
        cells = row.find_elements(By.TAG_NAME,value="td")
        row_data = [cell.text for cell in cells]
        table1_data.append(row_data)
    print(table1_data)

    expected_table1_data = [
        ["1", "40,800"],
        ["2", "53,400"],
        ["3", "69,100"],
        ["4", "90,000"],
    ]
    assert table1_data == expected_table1_data, "Table data does not match expected data."


    table2 = driver.find_element(By.XPATH,value="//*[@id='sib_case_study']/div/div[8]/table")

    # Get all the rows of the table except for the first row (heading row)
    rows_table2 = table2.find_elements(By.XPATH,value="//*[@id='sib_case_study']/div/div[8]/table/tbody/tr")

    # Initialize a list to store the table data
    table2_data = []

    # Iterate through the rows and extract cell data
    for row in rows_table2:
        # Get all the cells (columns) in the row
        # cells = row.find_elements(By.XPATH,value="//*[@id='sib_case_study']/div/div[6]/div[1]/table//td")
        cells = row.find_elements(By.TAG_NAME,value="td")

    
        second_column_text = cells[1].text
        third_column_text = cells[2].text
        table2_data.append([second_column_text, third_column_text])
    print(table2_data)

    # Define your expected table data as a list of lists, excluding the header row
    expected_table2_data = [
        ["120", "160"],
        ["0", "200,000"],
        ["0", "100,000"],
        ["0", "200,000"],
    ]

    # Verify the table data matches the expected data
    assert table2_data == expected_table2_data, "Table data does not match expected data."



    next_btn = driver.find_element(By.XPATH,value="//div[@class='buttonContainer']//button[@class='nextButton theme-font15'][normalize-space()='Next']")
    print("Next Button clicked")
    next_btn.click()
    time.sleep(5)