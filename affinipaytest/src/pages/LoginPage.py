from src.pages.InvoiceListPage import InvoiceListPage
from playwright.sync_api import Page, Response

class LoginPage:

    def __init__(self, page):
        self.page = page

    def __init__(self, page):
        self.page = page 
        self._username = page.locator("input[name=\"username\"]")
        self._password = page.locator("input[name=\"password\"]")
        self._login_btn = page.get_by_role("button", name="Login")
        self._error_alert_locator = page.get_by_role("alert")

    def enter_username(self, username):
        self._username.clear()
        self._username.fill(username)

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)

    def click_login(self):
        self._login_btn.click()
    
    def do_login(self, credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])
        self.click_login()
        return InvoiceListPage(self.page)
    
    @property
    def error_alert_locator(self):
        return self._error_alert_locator
    