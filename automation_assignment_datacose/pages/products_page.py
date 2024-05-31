from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    def select_first_product(self):
       self.page.click("div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] span[class='a-size-medium a-color-base a-text-normal']")

    def add_to_basket(self):
        self.page.click("input[id='add-to-cart-button']")