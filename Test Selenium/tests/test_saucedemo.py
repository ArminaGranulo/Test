from pages.home_page import HomePage

def test_correct_login(driver):
    home_page = HomePage(driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_title_1() == "PRODUCTS"
    home_page.add_to_cart("add_to_cart_1", "add_to_cart_2")
    home_page.click_cart_icon()
    assert home_page.get_title_2() == "YOUR CART"
    assert home_page.get_product_1() == "Sauce Labs Bolt T-Shirt"
    assert home_page.get_product_2() == "Sauce Labs Fleece Jacket"
    home_page.click_checkout_button()
    assert home_page.checkout_button() == "CHECKOUT: YOUR INFORMATION"
    home_page.fill_fields("Armina", "Granulo", "71212")
    home_page.click_continue_button()
    assert home_page.checkout_button() == "CHECKOUT: OVERVIEW"
    assert home_page.get_product_1_1() == "CHECKOUT: OVERVIEW"
    assert home_page.get_product_2_1() == "CHECKOUT: OVERVIEW"
    home_page.click_finish_button()
    assert home_page.checkout_complete() == "CHECKOUT: COMPLETE!"
    home_page.click_menu_button()
    home_page.logout_button()
    assert home_page.login_page() == "Accepted usernames are:"


