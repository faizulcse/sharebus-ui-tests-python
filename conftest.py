import os

import pytest

from src.setup.driver_setup import DriverSetup
from src.utils.file_helper import FileHelper


def pytest_addoption(parser):
    parser.addoption("--BASE_URL", action="store", default=os.getenv("BASE_URL"))
    parser.addoption("--BROWSER", action="store", default=os.getenv("BROWSER"))
    parser.addoption("--HEADLESS", action="store", default=os.getenv("HEADLESS"))
    parser.addoption("--DETACH", action="store", default=os.getenv("DETACH"))
    parser.addoption("--IMPLICIT_WAIT", action="store", default=os.getenv("IMPLICIT_WAIT"))
    parser.addoption("--EXPLICIT_WAIT", action="store", default=os.getenv("EXPLICIT_WAIT"))


@pytest.fixture(autouse=True)
def driver_handler(request):
    pytest.config = request.config
    base_url = pytest.config.getoption("--BASE_URL")
    imp_wait = int(pytest.config.getoption("--IMPLICIT_WAIT"))

    print("\n==============start_driver============>")
    driver = DriverSetup().get_driver(pytest)
    driver.implicitly_wait(imp_wait)
    driver.maximize_window()
    driver.get(base_url)

    pytest.driver = driver
    pytest.root_dir = os.path.dirname(os.path.abspath(__file__))
    pytest.testcase = os.environ.get("PYTEST_CURRENT_TEST").split("::")[2].split(" ")[0]

    yield
    print("\n=======take_screenshot_on_failed======>")
    FileHelper().take_screenshot(pytest)

    print("==============quit_driver=============>")
    detach = pytest.config.getoption("--DETACH")
    if detach == "false" and pytest.driver is not None:
        pytest.driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    result = outcome.get_result()
