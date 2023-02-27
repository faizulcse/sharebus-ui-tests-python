from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def print_title(self):
        print(self.get_title())
