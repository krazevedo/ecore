

class InvoiceListPage:

    def __init__(self, page):
        self.page = page
        self._invoice_list_header = page.locator("span")
        self._invoice_link_details = page.get_by_role("link", name="Invoice Details")

    def click_first_invoice_details_link(self):
        self._invoice_link_details.first.click()    

    @property
    def invoice_list_header(self):
        return self._invoice_list_header

