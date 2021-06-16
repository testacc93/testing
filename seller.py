from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/home/ankur/chromedriver/chromedriver')
driver.get("https://mmseller.datavivservers.in/login")

def login(email, password):
    try:
        email_id = WebDriverWait(driver,2).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/app-root/app-login/div/div/div/div/div[2]/form/div[1]/div/input')
            )
        )
        email_id.send_keys(email)

        password_field = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div/div/div[2]/form/div[2]/div[1]/input')
        password_field.send_keys(password)

        login_button = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div/div/div[2]/form/button')
        login_button.click()
        note = WebDriverWait(driver,1).until(
            EC.presence_of_element_located(
                (By.ID,'toast-container')
            )
        )
        if note:
            print("login is working")

    except Exception as e:
        print(e)

login('ankurkumar@gmail.com', '74y2772')

def register(name_of_business,my_email, my_password, my_mobile, first_name, last_name, des, phone,):
    address = 'type c 58 by 4 barc colony'
    create_account = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div/div/div[2]/p/span')
    create_account.click()

    try:

        drop_down = WebDriverWait(driver,2).until(
            EC.presence_of_element_located(
                (By.XPATH,'/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/select')
            )
        )
        drop_down.click()
        ###### BUSINESS DETAILS ########
        # international = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/select/option[3]')
        nob = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/input[1]')
        nob.send_keys(name_of_business)
        email = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/input[2]')
        email.send_keys(my_email)
        password = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/input[3]')
        password.send_keys(my_password)
        mobile = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/div[1]/div/input')
        mobile.send_keys(my_mobile)

        ###### SELLER DETAILS ######
        name = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/div[2]/div[1]/div/input')
        name.send_keys(first_name)
        second_name = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/div[2]/div[2]/div/input')
        second_name.send_keys(last_name)
        designation = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/div[3]/div[1]/div/input')
        designation.send_keys(des)

        phone_no = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[2]/form/div[4]/div[2]/div[1]/input')
        phone_no.send_keys(phone)

        ######## COMPANY ADDRESS ##########
        address_list = address.split(' ')
        print(address_list)
        company_name = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[4]/form/input[1]')
        company_name.send_keys(name_of_business)
        address_1 = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[4]/form/input[2]')
        address_1.send_keys(address_list[0]+address_list[1]+address_list[2]+address_list[3]+address_list[4])
        address_2 = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[4]/form/input[3]')
        address_2.send_keys(address_list[5]+address_list[6])
        city = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[4]/form/input[4]')
        city.send_keys('Mumbai')
        country = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[4]/form/input[5]')
        country.send_keys('India')
        pincode = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[4]/form/input[6]')
        pincode.send_keys('401504')

        checkbox = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[6]/form/div[1]/div/input')
        for j in range(0,10):
            try:
                if checkbox.is_selected() == False:
                    checkbox.click()
                    break
                else:
                    time.sleep(1)

            except:
                pass
        delivery_checkbox = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[6]/form/div[2]/div[2]/input')
        for j in range(0,10):
            try:
                if delivery_checkbox.click() == False:
                    delivery_checkbox.click()
                    break
                else:
                    time.sleep(1)

            except:
                pass

        continue_button = driver.find_element_by_xpath('/html/body/app-root/app-signup/div/div/div[2]/div/div[7]')
        continue_button.click()

    except Exception as e:
        print(e)
    notif = driver.find_element_by_id('toast-container')
    if notif:
        print("Reg process is working")
    else:
        print('Reg process isnt working')

register('bnw','ankur@gmail.com','wdwhwwf','88778799','ankur','kumar','owner','9767788')