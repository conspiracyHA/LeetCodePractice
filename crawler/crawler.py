from utility import path_join
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from random import randint
import re
import os


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
    return int(match.group(1)) if match else None


def get_finished_problems():
    result = list()
    for file_name in os.listdir(path_join('problems')):
        match = re.search(r'(\d+)\.', file_name)
        result.append(int(match.group(1)))
    return result


def get_a_problem(problem_count):
    problem_index = randint(1, problem_count)
    finished_list = get_finished_problems()
    while problem_index in finished_list:
        problem_index = randint(1, problem_count)
    return problem_index


go_last_page(driver)
problem_count = get_last_problem_index(driver)
problem_index = get_a_problem(problem_count)


print(problem_index)



