import os


class FileHelper:
    def take_screenshot(self, pytest):
        screenshots_dir = pytest.working_dir + "/screenshots/"
        screenshot_name = screenshots_dir + pytest.testcase + "_" + pytest.config.getoption("--BROWSER") + ".png"
        try:
            os.makedirs(screenshots_dir)
        except OSError:
            pass
        pytest.driver.get_screenshot_as_file(screenshot_name)
