from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/home/ankur/chromedriver/chromedriver')
driver.get("https://mmseller.datavivservers.in/login")


###### LOGIN PAGE ######
try:
    email_field = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-login/div/div/div/div/div[2]/form/div[1]/div/input')
        )

    )
    email_field.send_keys('nisarghshah23@gmail.com')

    password_field = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div/div/div[2]/form/div[2]/div[1]/input')
    password_field.send_keys('nisargh')

    login_button = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div/div/div[2]/form/button')
    login_button.click()
except Exception as e:
    print(e)

####### DASHBOARD #######
try:
    dashboard_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[2]/a/small')
        )

    )
    dashboard_button.click()

    chart = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/div/div/div[4]/div/div[2]/div/div[1]/div/div[3]/div/canvas[2]')
    if chart:
        print("dashboard button is working")
    else:
        print("dashboard button is not working")
except Exception as e:
    print(e)

####### INVENTORY ########
try:
    inventory_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[3]/a/small')
        )

    )
    inventory_button.click()

    add_new_button = driver.find_element_by_xpath(
        '/html/body/app-root/app-seller-view-product/div/div/div[6]/div/div[1]/div/div[1]/button')
    if add_new_button:
        print("Inventory button is working")
    else:
        print("Inventory button is not working")
except Exception as e:
    print(e)

####### ORDERS ########
try:
    orders_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[4]/a/small')
        )

    )
    orders_button.click()

    order_id = driver.find_element_by_xpath(
        '/html/body/app-root/app-order-view/div/div/div[6]/div/div[2]/div/table/thead/tr/th[1]/small/p')
    if order_id:
        print("Orders button is working")
    else:
        print("Orders button is not working")
except Exception as e:
    print(e)

####### ADVERTISING ########
try:
    advertising_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[5]/a')
        )

    )
    advertising_button.click()

    campaign = driver.find_element_by_xpath(
        '/html/body/app-root/app-advertise/div/div/div[1]/p')
    if campaign:
        print("Advertising button is working")
    else:
        print("Advertising button is not working")
except Exception as e:
    print(e)

####### REPORT ########
try:
    report_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[6]/a/small')
        )

    )
    report_button.click()

    report = driver.find_element_by_xpath(
        '/html/body/app-root/app-report/div/p')
    if report:
        print("Report button is working")
    else:
        print("Report button is not working")
except Exception as e:
    print(e)

####### PERFORMANCE ########
try:
    performance_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[7]/a/small')
        )

    )
    performance_button.click()

    performance = driver.find_element_by_xpath(
        '/html/body/app-root/app-performance-activity/div/div/div/div[1]/div/div[1]/h1')
    if performance:
        print("Performance button is working")
    else:
        print("performance button is not working")
except Exception as e:
    print(e)

####### OFFER ########
try:
    offer_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/app-header/nav[2]/div/div/ul/li[8]/a')
        )

    )
    offer_button.click()

    offer = driver.find_element_by_xpath(
        '/html/body/app-root/app-view-offer-pricing/div/div/div[1]/div/div[1]/h4')
    if offer:
        print("Offer button is working")
    else:
        print("Offer button is not working")
except Exception as e:
    print(e)





