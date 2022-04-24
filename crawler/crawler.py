# from selenium.webdriver.chrome import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re


driver = Chrome()

url = 'https://leetcode.com/problemset/all/'
driver.get(url)


def go_last_page(driver):
    driver.implicitly_wait(2)
    page_navigation = driver.find_element_by_css_selector('nav[role=navigation]')
    last_button = page_navigation.find_element_by_css_selector('button:nth-child(9)')
    last_button.click()
    sleep(3)


def get_last_problem_index(driver):
    problem_container = driver.find_element_by_css_selector('div[role=rowgroup]')
    last_problem = problem_container.find_element_by_css_selector('div[role=row]:last-child')
    match = re.search(r'(\d+)\.', last_problem.text)
    return match.group(1) if match else None


go_last_page(driver)
index = get_last_problem_index(driver)
print(index)



