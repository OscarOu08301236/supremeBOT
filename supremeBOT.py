from selenium import webdriver

name = ""
email = ""
tel = ""

number = ""
expiration_month = ""
expiration_year = ""
cvv = ""

chromedriver_location = "/Users/oushaoqian/Downloads/chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2/mt26hz7la")

add_to_cart_button = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart_button).click()

time.sleep(2)

checkout_button = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(checkout_button).click()

name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)

email_xpath = '//*[@id="order_email"]'
driver.find_element_by_xpath(email_xpath).send_keys(email)



print("Web Driver Run")