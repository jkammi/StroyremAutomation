import allure
from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase


class UsersAdminPage(SeleniumBase):

    # в __init__ храним название локатора и его значение для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # поле поиска
        self._admin_page_search_field = (By.CSS_SELECTOR, "#search [name=keyword]")
        self._admin_page_search_submit_button = (By.CSS_SELECTOR, "#search [type=submit]")
        # чекбокс юзера
        self._user_admin_page_checkbox = (By.CSS_SELECTOR, '.checkbox [type="checkbox"]')
        # выпадающий список для дальнейших действий с юзером
        self._admin_page_open_drop_down = (By.CSS_SELECTOR, "#action [name=action]")
        self._admin_page_drop_down_delete_option = (By.CSS_SELECTOR, "#action [name=action] [value=delete]")
        self._admin_page_apply_button = (By.CSS_SELECTOR, "#apply_action.button_green")


    @allure.step('Нахождение элемента: поле "Поиск" в панели админа на странице "Покупатели"')
    def get_admin_page_search_field(self):
        return self.find_element(self._admin_page_search_field)

    @allure.step('Нахождение элемента: кнопка "Поиск" в панели админа на странице "Покупатели"')
    def get_admin_page_search_submit_button(self):
        return self.find_element(self._admin_page_search_submit_button)

    @allure.step('Нахождение элемента: поле "Выпадающий список опций" в панели админа на странице "Покупатели"')
    def get_admin_page_open_drop_down(self):
        return self.find_element(self._admin_page_open_drop_down)

    @allure.step('Нахождение элемента: кнопка "Удалить в Выпадающем списке опций" в панели админа на странице "Покупатели"')
    def get_admin_page_drop_down_delete_option(self):
        return self.find_element(self._admin_page_drop_down_delete_option)

    @allure.step('Нахождение элемента: поле "Применить" в панели админа на странице "Покупатели"')
    def get_admin_page_apply_button(self):
        return self.find_element(self._admin_page_apply_button)

    @allure.step('Нахождение элемента: чекбокс юзера в панели админа на странице "Покупатели"')
    def get_user_admin_page_checkbox(self):
        return self.find_element(self._user_admin_page_checkbox)
