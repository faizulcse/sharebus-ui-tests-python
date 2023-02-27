from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverSetup:
    def get_driver(self, data):
        browser = data.getoption("--BROWSER").lower()
        headless = data.getoption("--HEADLESS").lower()
        detach = data.getoption("--DETACH").lower()
        match browser:
            case "chrome":
                service = Service(ChromeDriverManager().install())
                options = webdriver.ChromeOptions()
                if headless == "true":
                    options.add_argument('--headless')
                if detach == "true":
                    options.add_experimental_option("detach", True)
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                return webdriver.Chrome(service=service, options=options)
            case "firefox":
                service = Service(GeckoDriverManager().install())
                options = webdriver.FirefoxOptions()
                if headless == "true":
                    options.add_argument('--headless')
                return webdriver.Firefox(service=service, options=options)
            case "edge":
                service = Service(EdgeChromiumDriverManager().install())
                options = webdriver.EdgeOptions()
                if headless == "true":
                    options.add_argument('--headless')
                if detach == "true":
                    options.add_experimental_option("detach", True)
                return webdriver.Edge(service=service, options=options)
            case _:
                print("Invalid browser name: ====> " + browser)
