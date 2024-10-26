

class InvoiceDetailsPage:

    def __init__(self, page):
        self.page = page
        self._invoice_hotel_name = page.locator("h4")
        self._invoice_number_details = page.locator("h6")
        self._invoice_section = page.locator("section")
        self._invoice_booking_details_row = page.get_by_role("row")

    def check_booking_details_row(self, locator):
        return self._invoice_booking_details_row.filter(has_text=locator)    

    @property
    def check_hotel_name(self):
        return self._invoice_hotel_name
    
    @property
    def check_invoice_number(self):
        return self._invoice_number_details
    
    @property
    def check_section(self):
        return self._invoice_section

