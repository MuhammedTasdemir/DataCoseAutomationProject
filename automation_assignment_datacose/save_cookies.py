from playwright.sync_api import sync_playwright

def save_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.amazon.com")
        
        input("Complete the CAPTCHA and press Enter...")
        
        cookies = context.cookies()
        with open('cookies.json', 'w') as f:
            import json
            json.dump(cookies, f)
        
        browser.close()

if __name__ == "__main__":
    save_cookies()
