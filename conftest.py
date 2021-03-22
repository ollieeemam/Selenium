from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome driver...........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox driver...........")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):     # get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):      #return the browser value to setup method
    return request.config.getoption("--browser")


##### THML Report #####

def pytest_configure(config):      #adding environment info to the HTML report
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ollie Eemam'

@pytest.mark.optionalhook
def pytest_metadata(metadata):   #it hooks for delete/modify environment info to html report
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)