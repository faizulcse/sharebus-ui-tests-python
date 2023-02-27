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
    pytest.data = request.config
    base_url = request.config.getoption("--BASE_URL")
    imp_wait = int(request.config.getoption("--IMPLICIT_WAIT"))
    detach = request.config.getoption("--DETACH")

    driver = DriverSetup().get_driver(request.config)
    pytest.driver = driver
    driver.implicitly_wait(imp_wait)
    driver.maximize_window()
    driver.get(base_url)

    yield
    if detach == "false" and pytest.driver is not None:
        pytest.driver.quit()
