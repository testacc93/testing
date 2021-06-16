from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='/home/ankur/chromedriver/chromedriver')
driver.get("https://mmwebsite.datavivservers.in/")


######## SEARCH TAB #########
def search_bar(search_item):
    try:
        search_bar = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[1]/div/div[1]/div[2]/div/div[1]/form/div[1]/input')
        search_bar.send_keys(search_item)
        # suggestion_box = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[1]/div/div[1]/div[2]/div/div[1]/form/div[2]')
        suggestion_box = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,"/html/body/app-root/div/app-header/div[1]/nav[1]/div/div[1]/div[2]/div/div[1]/form/div[2]")))

        if suggestion_box:
            print("search is working for input "+ search_item)

    except Exception as e:
        print("search is not working for input " + search_item)
search_bar('bu')
######## SIGN IN ############

def signin(email, password):
    try:
        # driver.find_element_by_xpath('/html/body/app-root/div/div/app-login/div/div[1]/div/div/div[2]/div[1]/p[1]')
        sign_in_button = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/div/div/p[8]/small')
        time.sleep(2)
        sign_in_button.click()
        email_id_field = driver.find_element_by_xpath(
            '/html/body/app-root/div/div/app-login/div/div[1]/div/div/div[2]/div[1]/form/div[1]/div/input')
        email_id_field.send_keys(email)
        password_field = driver.find_element_by_xpath(
            '/html/body/app-root/div/div/app-login/div/div[1]/div/div/div[2]/div[1]/form/div[2]/div[1]/input')
        password_field.send_keys(password)
        login_button = driver.find_element_by_xpath(
            '/html/body/app-root/div/div/app-login/div/div[1]/div/div/div[2]/div[1]/form/button')
        login_button.click()
        print("Sign in button working")
    except Exception as e:
        print(e)

signin("djwfj@gmail.com", "password")

######## BRAND ############
try:
    brand_button = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[1]/a/small')
    brand_button.click()
    brands_label = driver.find_element_by_xpath('/html/body/app-root/div/div/app-allbrand/div/div/div/div/div[1]/div/div/div[1]/h1')
    if brands_label:
        print("brands button is working")

except Exception as e:
    print(e)


######## NEW ARRIVALS ##########
try:
    arrivals_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[2]/a/small"))
    )
    # arrivals_button = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[3]/a/small')
    arrivals_button.click()
    arrivals_label = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/div/div/app-new-arrival/div/div/div[3]/div[1]/h1"))
    )
    # arrivals_label = driver.find_element_by_xpath('/html/body/app-root/div/div/app-new-arrival/div/div/div[3]/div[1]/h1')
    if arrivals_label:
        print("new arrivals button is working")

except Exception as e:
    print(e)

###### OFFERS AND SALES #########
try:
    offers_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[3]/a/small"))
    )
    # offers_button = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[4]/a/small')
    offers_button.click()
    offers_label = driver.find_element_by_xpath('/html/body/app-root/div/div/app-offer-and-sales/div/div/div[1]/h1')
    if offers_label:
        print("offers and sales button is working")

except Exception as e:
    print(e)

####### trending products ##########
try:
    trending_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[5]/a/small"))
    )
    # trending_button = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[5]/a/small')
    trending_button.click()
    trending_label = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/div/div/app-new-arrival/div/div/div[3]/div[1]/h1"))
    )
    # trending_label = driver.find_element_by_xpath('/html/body/app-root/div/div/app-new-arrival/div/div/div[3]/div[1]/h1')
    if trending_label:
        print("Trending button is working")

except Exception as e:
    print(e)

########## JUST SOLD ############
try:
    just_sold_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[5]/a/small"))
    )
    # just_sold_button = driver.find_element_by_xpath('/html/body/app-root/div/app-header/div[1]/nav[2]/div/div/ul/li[6]/a/small')
    just_sold_button.click()
    # time.sleep(4)
    just_sold_label = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.ID, "title"))
    )
    if just_sold_label:
        print("Just sold button is working")

except Exception as e:
    print(e)

######## LOGIN PROCEDURE #########

from selenium.webdriver.common.action_chains import ActionChains
######## PRODUCTS PAGE ###########
try:
    time.sleep(5)
    # logo = WebDriverWait(driver,2).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH,'/html/body/app-root/div/div/app-new-arrival/div/div/div[3]/div[3]/div[2]/div/div[2]/div/div[2]/div/div/p[1]'))
    # )

    # print("the logo is", logo)
    # ActionChains(driver).move_to_element(logo).click(logo).perform()
    # logo.click()

    value_widget = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div/input[2]')
        )
    )
    value_before_inc = value_widget.get_attribute('value')
    # print(value_before_inc)
    increment_button = WebDriverWait(driver,2).until(
        EC.presence_of_element_located(
            (By.XPATH,'/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div/input[3]')
        )
    )

    increment_button.click()
    value_after_inc = value_widget.get_attribute('value')
    if str(value_after_inc) == '2':
        print("Increment button is working")
    # decrement_button = driver.find_element_by_xpath('/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div/input[1]')
    decrement_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div/input[1]')
        )
    )
    decrement_button.click()
    value_after_dec = value_widget.get_attribute('value')
    if str(value_after_dec) == '1':
        print("decrement button is working")
except Exception as e:
    print(e)


####### ADD TO CART ########
try:
    # add_to_cart_button = driver.find_element_by_xpath('/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[3]/button')
    add_to_cart_button = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH,
             '/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[3]/button')
        )
    )
    add_to_cart_button.click()
    # product_added_note = driver.find_element_by_id('toast-container')
    product_added_note = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located(
            (By.ID,
             'toast-container')
        )
    )
    if product_added_note:
        print("add to cart is not working")
    else:
        print("add to cart is working")
except Exception as e:
    print(e)


####### ADD TO WISHLIST ##########
try:
    wish_list_button = driver.find_element_by_xpath('/html/body/app-root/div/div/app-product/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div[4]/div/button')
    wish_list_button.click()
    login_popup = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             '/html/body/app-root/div/app-header/div[3]/div/div/div[2]/div/div[1]/p')
        )
    )
    if login_popup:
        print("Wishlist button is working")
    else:
        print("wishlist button isnt working")
except Exception as e:
    print(e)