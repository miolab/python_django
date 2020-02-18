import pytest
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions


options = FirefoxOptions()
driver = Firefox(options=options)


def test_browser_get():
    """ red (if django YET started)
    """
    driver.get('http://127.0.0.1:8000/')
    assert "Django" in driver.title


# dviver.quit()