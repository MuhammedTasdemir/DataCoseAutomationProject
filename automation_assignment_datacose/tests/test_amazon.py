import pytest
import json
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.basket_page import BasketPage

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    
    with open('cookies.json', 'r') as f:
        cookies = json.load(f)
        context.add_cookies(cookies)
    
    page.goto("https://www.amazon.com")
    yield page
    page.close()

def test_amazon(page):
    home_page = HomePage(page)
    product_page = ProductsPage(page)
    basket_page = BasketPage(page)

    home_page.navigate()
    home_page.search_product("keyboard")
    product_page.select_first_product()
    product_page.add_to_basket()
    basket_page.navigate_to_basket()
    basket_page.update_quantity(5)
    assert basket_page.get_quantity() == "5"