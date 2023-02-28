import os

import pytest

from src.setup.driver_setup import DriverSetup


def pytest_addoption(parser):
    parser.addoption("--BASE_URL", action="store", default=os.getenv("BASE_URL"))
    parser.addoption("--BROWSER", action="store", default=os.getenv("BROWSER"))
    parser.addoption("--HEADLESS", action="store", default=os.getenv("HEADLESS"))
    parser.addoption("--DETACH", action="store", default=os.getenv("DETACH"))
    parser.addoption("--IMPLICIT_WAIT", action="store", default=os.getenv("IMPLICIT_WAIT"))
    parser.addoption("--EXPLICIT_WAIT", action="store", default=os.getenv("EXPLICIT_WAIT"))


@pytest.fixture(autouse=True)
def driver_handler(request):
    browser = request.config.getoption("--BROWSER").lower()
    base_url = request.config.getoption("--BASE_URL")
    detach = request.config.getoption("--DETACH")
    imp_wait = int(request.config.getoption("--IMPLICIT_WAIT"))
    pytest.data = request.config

    print("==============start_driver======>")
    driver = DriverSetup().get_driver(browser)
    driver.implicitly_wait(imp_wait)
    driver.maximize_window()
    driver.get(base_url)
    pytest.driver = driver

    yield
    if detach == "false" and pytest.driver is not None:
        print("==============quit_driver======>")
        pytest.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        print("<======take_screenshot_on_failed=====>")
