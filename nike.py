from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import config as Config
import time

path = r'geckodriver.exe'
# max_timeout = Config.MAX_TIMEOUT
main_driver = webdriver.Firefox(executable_path=path)


def check_location():
    try:
        #check to see if location is valid, important because each site is different.
        location = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//span[@data-qa="locale-selctor-active-country-label"]'))
        if location.text == 'United States':
            print("Location is valid")
            return True
        else:
            print("CHANGE LOCATION TO UNITED STATES")
            return False
    except TimeoutException:
        return False


def check_size(shoe_size):
    MF_size_dict = {
    '9':'//button[@class="size-grid-dropdown size-grid-button"][.="M 9 / W 10.5"]', 
    '9.5': '//button[@class="size-grid-dropdown size-grid-button"][.="M 9.5 / W 11"]',
    '10': '//button[@class="size-grid-dropdown size-grid-button"][.="M 10 / W 11.5"]',
    '10.5': '//button[@class="size-grid-dropdown size-grid-button"][.="M 10.5 / W 12"]',
    '11.5': '//button[@class="size-grid-dropdown size-grid-button"][.="M 11.5 / W 13]',
    '12': '//button[@class="size-grid-dropdown size-grid-button"][.="M 12 / W 13.5"]',
    '12.5': '//button[@class="size-grid-dropdown size-grid-button"][.="M 12.5 / W 14"]'
    }
    try:
        #check to see if location is valid, important because each nike site version is different.
        size = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    MF_size_dict.get(shoe_size)
                )
            )

        try:
            time.sleep(2)
            size.click()
        except ElementClickInterceptedException:
            print('%s NOT AVAILABLE' % shoe_size)
            if shoe_size == Config.SECONDARY_TARGET_SIZE:
                return False
            else:
                return check_size(Config.SECONDARY_TARGET_SIZE)

    except TimeoutException:
        print('%s NOT AVAILABLE' % shoe_size)
        if shoe_size == Config.SECONDARY_TARGET_SIZE:
            return False
        else:
            return check_size(Config.SECONDARY_TARGET_SIZE)
    
    print("Size %s found" % shoe_size)
    return True

def check_if_ready():
    try:
        #check to see if item is available on the site
        cart_button = WebDriverWait(
            main_driver, 5).until(
                lambda driver: driver.find_element_by_xpath(
                    '//button[@data-qa="add-to-cart"]'))
    except TimeoutException:
        print("Not ready")
        return False
    return True

def check_availability():
    try:
        #check to see if item is available on the site
        cart_button = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//button[@data-qa="add-to-cart"]'))
        #if button is found click button to move to next page.
        cart_button.click()
    except TimeoutException:
        print("Could not find cart")
        return False
    return True


def checkout():
    try:
        #check to see if item is available on the site
        checkout_button = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//button[@data-qa="checkout-link"]'))
        #if button is found click button to move to next page.
        checkout_button.click()
    except TimeoutException:
        print("Could not find checkout")
        return False
    return True


def checkout_guest():
    try:
        #check to see if item is available on the site
        checkout_button = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//button[@id="qa-guest-checkout"]'))
        #if button is found click button to move to next page.
        checkout_button.click()
    except TimeoutException:
        print("Could not find checkout guest button")
        return False
    return True

def address():
    main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        #do this first to make sure whether page has loaded
        first = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//input[@id="firstName"]'))
        first.send_keys(Keys.CONTROL + "a")
        first.send_keys(Keys.DELETE)
        first.send_keys(Config.FIRST_NAME)
    except TimeoutException:
        print("Error in finding first name.")
        return False
    
    main_driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(Keys.DELETE)

    main_driver.find_element_by_xpath('//a[@id="addressSuggestionOptOut"]').click()

    main_driver.find_element_by_xpath('//input[@id="address1"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="address1"]').send_keys(Keys.DELETE)
    
    main_driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys(Keys.DELETE)

    main_driver.find_element_by_xpath('//input[@id="city"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="city"]').send_keys(Keys.DELETE)

    main_driver.find_element_by_xpath('//input[@id="email"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="email"]').send_keys(Keys.DELETE)

    main_driver.find_element_by_xpath('//input[@id="postalCode"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="postalCode"]').send_keys(Keys.DELETE)


    main_driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(Config.LAST_NAME)
    main_driver.find_element_by_xpath('//input[@id="address1"]').send_keys(Config.STREET_ADDRESS)
    # main_driver.find_element_by_xpath('//input[@id="addressLineTwo"]').send_keys(Config.APT)
    main_driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys(Config.PHONE)
    main_driver.find_element_by_xpath('//input[@id="city"]').send_keys(Config.CITY)
    main_driver.find_element_by_xpath('//input[@id="email"]').send_keys(Config.EMAIL)
    main_driver.find_element_by_xpath('//input[@id="postalCode"]').send_keys(Config.ZIP_CODE)

    if Config.APT != '':
        # main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element=WebDriverWait(main_driver,30).until(EC.element_to_be_clickable((By.XPATH,'//span[@class="d-sm-ib"]')))
        element.location_once_scrolled_into_view
        element.click()
        # time.sleep(1)
        # main_driver.find_element_by_xpath('//span[@class="d-sm-ib"]').click()
        main_driver.find_element_by_xpath('//input[@id="address2"]').send_keys(Keys.CONTROL + "a")
        main_driver.find_element_by_xpath('//input[@id="address2"]').send_keys(Keys.DELETE)
        main_driver.find_element_by_xpath('//input[@id="address2"]').send_keys(Config.APT)
    
    select = Select(
        main_driver.find_element_by_xpath(
        '//select[@id="state"]'))
    select.select_by_visible_text(Config.STATE)

    #continue button
    continue_button = main_driver.find_element_by_xpath('//button[@class="js-next-step saveAddressBtn mod-ncss-btn ncss-btn-accent ncss-brand pt3-sm prl5-sm pb3-sm pt2-lg pb2-lg d-md-ib u-uppercase u-rounded fs14-sm mod-button-width"]')
    continue_button.click()

    return True


# Automatically going with whatever site chooses
def shipping():
    main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)
    try:
        #check to see if item is available on the site
        cheap_shipping = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//button[@type="button"][.="Continue to Payment"]'
            )
        )
        #if button is found click button to move to next page.
        time.sleep(1)
        cheap_shipping.click()

        # main_driver.execute_script("arguments[0].click();",cheap_shipping)
    except TimeoutException:
        print("Could not find continue")
        return False
    return True

def payment_billing_addr_unchanged():
    try:
        #do this to check if new section has popped up.
        main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        credit = WebDriverWait(
            main_driver, 20).until(
                lambda driver: driver.find_element_by_xpath(
                    '//label[@for="paypal"]'))
        # credit.click()
    except TimeoutException:
        print("Error in using card section")
        # main_driver.close()
        return False
    time.sleep(3)
    main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element=WebDriverWait(main_driver,30).until(EC.element_to_be_clickable((By.XPATH,'//input[@data-shortname="cc"]')))
    element.location_once_scrolled_into_view
    element.click()
    main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # main_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # main_driver.find_element_by_xpath('//input[@id="firstName"]').send_keys(Keys.CONTROL + "a")
    # main_driver.find_element_by_xpath('//input[@id="firstName"]').send_keys(Keys.DELETE)
    # main_driver.find_element_by_xpath('//input[@id="firstName"]').send_keys(Config.FIRST_ON_CARD)

    # main_driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(Keys.CONTROL + "a")
    # main_driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(Keys.DELETE)
    # main_driver.find_element_by_xpath('//input[@id="lastName"]').send_keys(Config.LAST_ON_CARD)

    main_driver.find_element_by_xpath('//input[@data-shortname="cc"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@data-shortname="cc"]').send_keys(Keys.DELETE)
    main_driver.find_element_by_xpath('//input[@data-shortname="cc"]').send_keys(Config.CARD_NUMBER)

    main_driver.find_element_by_xpath('//input[@id="cvNumber"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="cvNumber"]').send_keys(Keys.DELETE)
    main_driver.find_element_by_xpath('//input[@id="cvNumber"]').send_keys(Config.CVV)

    # main_driver.find_element_by_xpath('//input[@id="phone"]').send_keys(Keys.CONTROL + "a")
    # main_driver.find_element_by_xpath('//input[@id="phone"]').send_keys(Keys.DELETE)
    # main_driver.find_element_by_xpath('//input[@id="phone"]').send_keys(Config.PHONE)
    main_driver.find_element_by_xpath('//input[@id="expirationDate"]').send_keys(Keys.CONTROL + "a")
    main_driver.find_element_by_xpath('//input[@id="expirationDate"]').send_keys(Keys.DELETE)
    main_driver.find_element_by_xpath('//input[@id="expirationDate"]').send_keys('%s/%s' % (Config.EXP_MONTH, Config.EXP_YEAR))



    # time.sleep(1)
    review_order_button = main_driver.find_element_by_xpath('//button[@data-attr="continueToOrderReviewBtn"]')
    review_order_button.click()
    return True



def launch(url):
    main_driver.get(url)

    check_location()
    while check_if_ready() == False:
        main_driver.refresh()
        print("Retrying Page")
    if check_size(Config.TARGET_SIZE) == False:
        print("Size not available")
        return
    check_availability()
    checkout()
    checkout_guest()
    address()
    if shipping() == False:
        print("Error in shipping")
    print("Script is done")
