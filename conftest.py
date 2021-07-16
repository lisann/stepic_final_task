import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language")

@pytest.fixture(scope="function")
def browser():
    user_language = {"languges": "en"}
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options, executable_path="/Users/katerina/Web/chromedriver2")
    # driver.implicitly_wait(5)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

