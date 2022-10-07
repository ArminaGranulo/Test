from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)
    
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def login(self, username, password):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.click()
        username_field.send_keys(username)
        password_field = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_field.clear()
        password_field.click()
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        login_button.click()
    
    def get_title_1(self):
        welcome_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return welcome_element.text

    def add_to_cart(self, add_to_cart_1, add_to_cart_2):
        add_to_cart_1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")))
        add_to_cart_1.click()
        add_to_cart_2 = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket")))
        add_to_cart_2.click()

    def click_cart_icon(self):
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        cart_icon.click()

    def get_title_2(self):
        welcome_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return welcome_element.text

    def get_product_1(self):
        product_1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item_1_title_link']/div")))
        return product_1.text
    
    def get_product_2(self):
        product_2 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='item_5_title_link']/div")))
        return product_2.text

    def click_checkout_button(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='checkout']")))
        checkout_button.click()

    def checkout_button(self):
        checkout_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))   
        return checkout_button.text

    def fill_fields(self, first_name, last_name, zip_postal_code):
        first_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name_field.clear()
        first_name_field.click()
        first_name_field.send_keys(first_name)
        last_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        last_name_field.clear()
        last_name_field.click()
        last_name_field.send_keys(last_name)
        zip_postal_code_field = self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        zip_postal_code_field.clear()
        zip_postal_code_field.click()
        zip_postal_code_field.send_keys(zip_postal_code)

    def click_continue_button(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='continue']")))
        continue_button.click()

    def checkout_overview(self):
        checkout_overview = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))   
        return checkout_overview.text

    def get_product_1_1(self):
        product_1_1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return product_1_1.text
    
    def get_product_2_1(self):
        product_2_1 = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        return product_2_1.text

    def click_finish_button(self):
        finish_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='finish']")))
        finish_button.click()

    def checkout_complete(self):
        checkout_complete = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))   
        return checkout_complete.text

    def click_menu_button(self):
        menu_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-burger-menu-btn']")))
        menu_button.click()

    def logout_button(self):
        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='logout_sidebar_link']")))
        logout_button.click()

    def login_page(self):
        login_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login_credentials']/h4")))   
        return login_page.text