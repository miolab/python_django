# // preparing //
# from hoge_main_app.py import *

import pytest
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
import time

options = FirefoxOptions()
driver = Firefox(options=options)


@pytest.fixture(scope="module", autouse=True)
def browser_run():
    print('// Functional test //')
    yield
    time.sleep(0.5)
    driver.quit()


@pytest.mark.skip(reason = "confirmed")
def test_browser_run_init(browser_run):
    driver.get('http://127.0.0.1:8000/')
    assert "Django" in driver.title


@pytest.mark.parametrize(
    "url", [
        ('http://127.0.0.1:8000/myapp/hello'),
        ('http://127.0.0.1:8000/myapp/temp')
    ]
)
def test_browser_views_init(browser_run, url):
    driver.get(url)
    # assert "Hello Red" in driver.page_source
    assert "Hello World" in driver.page_source

