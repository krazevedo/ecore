import pytest
from playwright.sync_api import Page, expect
from src.pages.LoginPage import LoginPage
from src.pages.InvoiceDetailsPage import InvoiceDetailsPage


@pytest.fixture()
def response():
    return {"HotelName": "Rendezvous Hotel", "InvoiceDate": "14/01/2018", "DueDate": "15/01/2018", "InvoiceNumber": "110", "BookingCode": "0875", 
            "CustomerDetails": "JOHNY SMITH R2, AVENUE DU MAROC 123456", "Room": "Superior Double", "CheckIn": "14/01/2018", "CheckOut": "15/01/2018",
            "TotalStayCount": "1", "TotalStayAmount": "$150", "DepositNow": "USD $20.90", "Tax&VAT": "USD $19.00","TotalAmount": "USD $209.00"}

def test_invoice_details(set_up_tear_down, response) -> None:
    credentials = {"username": "demouser", "password":"abc123"}
    page = set_up_tear_down  
    login = LoginPage(page)
    invoice_list_p = login.do_login(credentials)
    expect(invoice_list_p.invoice_list_header).to_have_text("Automation Example")

    with page.expect_popup() as page1_info:        
        invoice_list_p.click_first_invoice_details_link()
    
    page1 = page1_info.value

    invoice_details_p = InvoiceDetailsPage(page1)

    expect(invoice_details_p.check_hotel_name).to_contain_text(response.get("HotelName"))
    expect(invoice_details_p.check_invoice_number).to_contain_text(response.get("InvoiceNumber"))
    expect(invoice_details_p.check_section).to_contain_text(response.get("InvoiceDate"))
    expect(invoice_details_p.check_section).to_contain_text(response.get("DueDate"))
    expect(invoice_details_p.check_booking_details_row("Booking Code")).to_contain_text(response.get("BookingCode"))
    expect(invoice_details_p.check_booking_details_row("Room")).to_contain_text(response.get("Room"))
    expect(invoice_details_p.check_booking_details_row("Total Stay Count")).to_contain_text(response.get("TotalStayCount"))
    expect(invoice_details_p.check_booking_details_row("Total Stay Amount")).to_contain_text(response.get("TotalStayAmount"))
    expect(invoice_details_p.check_booking_details_row("Check-In")).to_contain_text(response.get("CheckIn"))
    expect(invoice_details_p.check_booking_details_row("Check-Out")).to_contain_text(response.get("CheckOut"))
    expect(invoice_details_p.check_section).to_contain_text(response.get("CustomerDetails"))
    expect(invoice_details_p.check_section).to_contain_text(response.get("DepositNow"))
    expect(invoice_details_p.check_section).to_contain_text(response.get("Tax&VAT"))
    expect(invoice_details_p.check_section).to_contain_text(response.get("TotalAmount"))