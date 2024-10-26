import pytest


@pytest.fixture()
def set_up_tear_down(page):
    # page.set_viewport_size({"width": 1536, "heigth": 800})
    page.goto("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/")
    yield page