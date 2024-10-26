import pytest
from playwright.sync_api import Page, expect
from src.pages.LoginPage import LoginPage

def test_login_positive(set_up_tear_down) -> None: 
    page = set_up_tear_down  
    credentials = {"username": "demouser", "password":"abc123"}
    login = LoginPage(page)
    invoice_list_p = login.do_login(credentials)
    expect(invoice_list_p.invoice_list_header).to_have_text("Automation Example")

@pytest.mark.parametrize("username, password", [("Demouser", "abc123"),("demouser_", "xyz"),("demouser", "nananana"),pytest.param("demouser", "abc123", marks=pytest.mark.xfail)])
def test_login_negative(set_up_tear_down, username, password) -> None:
    page = set_up_tear_down  
    credentials = {"username": username, "password":password}
    login = LoginPage(page)
    login.do_login(credentials)

    error_message = "Wrong username or password."
    expect(login.error_alert_locator).to_have_text(error_message)