from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/home/ankur/chromedriver/chromedriver')
driver.get("https://www.techfactoryjr.com/")

# ###### HOME BUTTON #######
try:
    home_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[1]/a/span')
        )

    )
    home_button.click()
    foundation_of_future = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/article/div/div/div/section[2]/div[3]/div/div/section[1]/div/div/div/div/div/h2')
        )
    )
    if foundation_of_future:
        print("home button is working")

except Exception as e:
    print(e)

####### WHO WE ARE #########
try:
    who_we_are_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[2]/a/span')
        )

    )
    who_we_are_button.click()
    about_dataviv = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/section[1]/div[2]/div[2]/div/div[1]/div/h2')
        )
    )
    if about_dataviv:
        print("who we are? button is working")

except Exception as e:
    print(e)

###### WHAT WE DO #######
try:
    what_we_do_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[3]/a/span')
        )

    )
    what_we_do_button.click()
    data_servives = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/article/div/div/div/section[1]/div[3]/div/div/section[1]/div/div/div/div[2]/div/h2')
        )
    )
    if data_servives:
        print("what we do? button is working")

except Exception as e:
    print(e)

###### OUR WORK ######
try:
    our_work_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[4]/a/span')
        )

    )
    our_work_button.click()
    we_make_dreams_reality = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/section/div[3]/div/div/section[1]/div/div[2]/div/div/div/h2')
        )
    )
    if we_make_dreams_reality:
        print("Our work button is working")

except Exception as e:
    print(e)

###### BLOG #######
try:
    blog_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[5]/a/span')
        )

    )
    blog_button.click()
    checkout_our_blog = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/section[2]/div/div[1]/div/div/div/h2')
        )
    )
    if checkout_our_blog:
        print("Blog button is working")

except Exception as e:
    print(e)

#### CAREERS ######
try:
    careers_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[6]/a/span')
        )

    )
    careers_button.click()
    culture = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/section[2]/div[2]/div/div/section[1]/div/div/div/div[2]/div/h2')
        )
    )
    if culture:
        print("Careers button is working")

except Exception as e:
    print(e)

###### WRITE TO US #########
try:
    write_to_us_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/header/div/div[1]/div/nav/ul/li[7]/a/span')
        )

    )
    write_to_us_button.click()
    contact = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/article/div/div/div/section[2]/div[3]/div[2]/div/div[2]/div/h2')
        )
    )
    if contact:
        print("Contact button is working")

except Exception as e:
    print(e)

###### KNOW MORE ######
try:
    work_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/header/div/div[1]/div/nav/ul/li[4]/a/span')
        )
    )
    work_button.click()
    # print('working till work button click')
    know_more = WebDriverWait(driver,5).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div/section/div[3]/div/div/section[3]/div/div[1]/div/div[2]/div/div/a')
        )
    )
    know_more.click()
    ai_text = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/div/div/section[1]/div[2]/div/div/div[1]/div/h2')
        )
    )
    if ai_text:
        print("Know more button for AI is working")
except Exception as e:
    print(e)


