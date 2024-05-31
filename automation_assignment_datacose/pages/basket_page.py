from playwright.sync_api import Page

class BasketPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_basket(self):
        self.page.click("a[id='nav-cart']")

    def update_quantity(self, quantity: int):
        self.page.select_option("select[name='quantity']", str(quantity))

    def get_quantity(self):
        return self.page.input_value("select[name='quantity']")