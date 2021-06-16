from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/home/ankur/chromedriver/chromedriver')
driver.get("https://www.techfactorysr.com/")


####### READ MORE #######
try:
    readmore_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div/section[5]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/a[2]')
        )

    )
    readmore_button.click()
    take_this_course_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/section/div[2]/div/main/article/div/div/div/div[2]/div[2]/form/button')
        )
    )
    take_this_course_button.click()
    login_popup = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div/div[1]/div[1]/h4')
        )
    )


    if login_popup:
        print("take this course button is working")

except Exception as e:
    print(e)

# ###### ABOUT US #######
try:
    about_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/header/div[2]/div/div/div/nav/ul/li[2]/a')
        )

    )
    about_button.click()

    our_story = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/section/div[2]/div/main/article/div/div/div/section[1]/div/div/div/div[1]/div/div/h3')
        )
    )
    if our_story:
        print("About us button is working")

except Exception as e:
    print(e)

###### COURSES ##########
try:
    courses_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/header/div[2]/div/div/div/nav/ul/li[2]/a')
        )

    )
    courses_button.click()

    all_courses = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/section/div[1]/div[1]/div/div/h1')
        )
    )
    if all_courses:
        print("All courses button is working")

except Exception as e:
    print(e)

##### CAREER ######
try:
    career_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/header/div[2]/div/div/div/nav/ul/li[5]/a')
        )

    )
    career_button.click()

    careers = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/section/div[2]/div/main/article/div/div/div/section[1]/div/div/div/div/div/div/h3')
        )
    )
    if careers:
        print("Careers button is working")

except Exception as e:
    print(e)

####### CONTACT ########
try:
    contact_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/header/div[2]/div/div/div/nav/ul/li[6]/a')
        )

    )
    contact_button.click()

    contact_info = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/section/div[2]/div/main/article/div/div/div/section[1]/div/div[1]/div/div[1]/div/div/h3')
        )
    )
    if contact_info:
        print("Contact button is working")

except Exception as e:
    print(e)

###### REGISTER ########
try:
    register_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/header/div[1]/div/div/div/div/aside[2]/div/div/a[1]')
        )

    )
    register_button.click()

    register_popup = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/h4')
        )
    )
    if register_popup:
        print("Register button is working")

except Exception as e:
    print(e)

###### LOGIN #######
try:
    login_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/header/div[1]/div/div/div/div/aside[2]/div/div/a[2]')
        )

    )
    login_button.click()

    login_popup = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[3]/div/div/div[1]/div[1]/h4')
        )
    )
    if login_popup:
        print("Login button is working")

except Exception as e:
    print(e)
