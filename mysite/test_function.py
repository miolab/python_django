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


@pytest.mark.skip(reason = "confirmed")
@pytest.mark.parametrize(
    "url", [
        ('http://127.0.0.1:8000/myapp/hello'),
        ('http://127.0.0.1:8000/myapp/temp'),
        ('http://127.0.0.1:8000/myapp/query/?user=IM&message=Hello.')
    ]
)
def test_browser_views_init(browser_run, url):
    driver.get(url)
    # assert "Red" in driver.page_source
    assert "Hello" in driver.page_source


@pytest.mark.skip(reason = "confirmed")
@pytest.mark.parametrize(
    "url", [
        ('http://127.0.0.1:8000/admin')
    ]
)
def test_admin(browser_run, url):
    driver.get(url)
    assert "Username" in driver.page_source


@pytest.mark.skip(reason = "confirmed")
@pytest.mark.parametrize(
    "url", [
        ('http://127.0.0.1:8000/myapp/article'),
        ('http://127.0.0.1:8000/myapp/article/add'),
        ('http://127.0.0.1:8000/myapp/article/modify/1'),
        ('http://127.0.0.1:8000/myapp/article/del/1')
    ]
)
def test_admin(browser_run, url):
    driver.get(url)
    assert "投稿記事" in driver.page_source




@pytest.mark.parametrize(
    "url", [
        ('http://127.0.0.1:8000/myapp/article'),
    ]
)
def test_crud(browser_run, url):
    driver.get(url)
    assert "投稿記事の一覧" in driver.page_source

    add_btn = driver.find_element_by_id("addArticle")
    add_btn.click()
    time.sleep(0.1)
    assert "投稿記事の編集" in driver.page_source

    # // Test // Create
    input_title = driver.find_element_by_id("id_title_submit")
    input_title.send_keys("自動投稿テスト")
    input_text = driver.find_element_by_id("id_text_submit")
    input_text.send_keys("自動投稿テスト")
    time.sleep(0.1)
    submit_btn = driver.find_element_by_id("submitArticle")
    submit_btn.click()
    time.sleep(1)
    assert "自動投稿テスト" in driver.page_source

    # // Test // Update


    # // Test // Delete



