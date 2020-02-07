from selenium import webdriver
from time import sleep
from parsel import Selector
import openpyxl


import parameters

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome()

# # driver.get method() will navigate to a page given by the URL address
# driver.get('https://www.linkedin.com')
# sleep(2)
#
# # locate submit button by_class_name
# sign_in_button = driver.find_element_by_class_name('nav__button-secondary')
#
# # .click() to mimic button click
# sign_in_button.click()
#
# # locate email form by_class_name
# username = driver.find_element_by_id('username')
#
#
# # send_keys() to simulate key strokes
# username.send_keys(parameters.linkedin_username)
#
# # locate password form by_class_name
# password = driver.find_element_by_id('password')
#
# # send_keys() to simulate key strokes
# password.send_keys(parameters.linkedin_password)
#
# # locate submit button by_class_name
# log_in_button = driver.find_element_by_class_name('login__form_action_container ')
#
# # .click() to mimic button click
# log_in_button.click()
#
# sleep(1)


driver.get('https://www.google.com/')

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys(parameters.search_query)
sleep(1)

search_query.submit()
sleep(1)

linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_url_for_excel = []

for i, url in enumerate(linkedin_urls):
    if i % 2 == 0:
        linkedinurl, username = url.text.split(' › ')
        linkedin_url_for_excel.append('https://' + linkedinurl +'/in/'+username)

sleep(1)

wb = openpyxl.Workbook()
ws = wb.active

for i, linkedin_url in enumerate(linkedin_url_for_excel):
    ws.cell(row=i+1, column=1, value=linkedin_url)

wb.save(parameters.file_name)







