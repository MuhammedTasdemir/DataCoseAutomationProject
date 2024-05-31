from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.amazon.com")

    def search_product(self, product_name: str):
        search_box = self.page.locator("#twotabsearchtextbox")
        search_box.fill(product_name)
        self.page.locator("input[id='nav-search-submit-button']").click()