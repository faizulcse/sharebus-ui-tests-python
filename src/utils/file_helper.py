import os


class FileHelper:
    def take_screenshot(self, pytest):
        screenshots_dir = pytest.root_dir + "/screenshots/"
        try:
            os.makedirs(screenshots_dir)
        except OSError:
            pass
        screenshot_name = pytest.testcase + "_" + pytest.config.getoption("--BROWSER") + ".png"
        pytest.driver.get_screenshot_as_file(screenshots_dir + screenshot_name)
