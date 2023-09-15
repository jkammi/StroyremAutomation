import allure
from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase


class SignUpPage(SeleniumBase):

    # в __init__ храним название локатора и его значение для необходимой страницы
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._main_page_sign_up_button = (By.CSS_SELECTOR, "a.register-link") # TODO Its duplicate from sign_in_page
        self._main_page_profile_icon = (By.CSS_SELECTOR, ".header-profile-link.auth-tooltip-show")# TODO Its duplicate from sign_in_page
        # Окно регистрации
        self._physical_user_button = (By.CSS_SELECTOR, ".reg-tab-title[data-tab=tab-1]")
        self._jur_user_button = (By.CSS_SELECTOR, ".reg-tab-title[data-tab=tab-2]")
        # # элементы регистрации физлица:
        self._name_field = (By.CSS_SELECTOR, ".registration-tab [name=name]")
        self._surname_field = (By.CSS_SELECTOR, ".registration-tab [name=family]")
        self._password_field = (By.CSS_SELECTOR, ".registration-tab [name=password]")
        self._phone_field = (By.CSS_SELECTOR, ".registration-tab [name=phone]")
        self._email_field = (By.CSS_SELECTOR, ".registration-tab [name=email]")
        self._club_card_number_field = (By.CSS_SELECTOR, ".registration-tab [name=card_number]")
        self._personal_data_agreement_checkbox = (By.CSS_SELECTOR, ".checkbox-item label[for=c1]")
        self._already_have_account_button = (By.CSS_SELECTOR, ".flex-row .yellow-btn-invert[href=#login-modal]")
        self._registration_button = (By.CSS_SELECTOR, ".yellow-btn[name=register_person]")
        self._error_message = (By.CSS_SELECTOR, ".message_error")
        self._error_message_missing_name = (By.CSS_SELECTOR, ".registration-tab input[name=name] + div.field-error")
        self._error_message_missing_surname = (By.CSS_SELECTOR, ".registration-tab input[name=family] + div.field-error")
        self._error_message_missing_password = (By.CSS_SELECTOR, ".registration-tab input[name=password] + div.field-error")
        self._error_message_missing_phone = (By.CSS_SELECTOR, ".registration-tab input[name=phone] + div.field-error")
        self._error_message_missing_email = (By.CSS_SELECTOR, ".registration-tab input[name=email] + div.field-error")
        # # элементы регистрации юрлица:
        # ...
        # ...
        # ...


    @allure.step("Нахождение элемента: кнопка 'Регистрация' в хедере")
    def get_main_page_sign_up_button(self):
        return self.find_element(self._main_page_sign_up_button)

    @allure.step("Нахождение элемента: иконка профиля в хедере")
    def get_main_page_profile_icon(self):
        return self.find_element(self._main_page_profile_icon)

    @allure.step("Нахождение элемента: поле 'Имя' окна регистрации Физического лица")
    def get_name_field(self):
        return self.find_element(self._name_field)

    @allure.step("Нахождение элемента: поле 'Фамилия' окна регистрации Физического лица")
    def get_surname_field(self):
        return self.find_element(self._surname_field)

    @allure.step("Нахождение элемента: поле 'Пароль' окна регистрации Физического лица")
    def get_password_field(self):
        return self.find_element(self._password_field)

    @allure.step("Нахождение элемента: поле 'Номер телефона' окна регистрации Физического лица")
    def get_phone_field(self):
        return self.find_element(self._phone_field)

    @allure.step("Нахождение элемента: поле 'Электронная почта' окна регистрации Физического лица")
    def get_email_field(self):
        return self.find_element(self._email_field)

    @allure.step("Нахождение элемента: поле 'Номер клубной карты' окна регистрации Физического лица")
    def get_club_card_number_field(self):
        return self.find_element(self._club_card_number_field)

    @allure.step("Нахождение элемента: чекбокс 'Я согласен на обработку моих персональных данных' окна регистрации Физического лица")
    def get_personal_data_agreement_checkbox(self):
        return self.find_element(self._personal_data_agreement_checkbox)

    @allure.step("Нахождение элемента: кнопка 'Уже есть аккаунт' окна регистрации Физического лица")
    def get_already_have_account_button(self):
        return self.find_element(self._already_have_account_button)

    @allure.step("Нахождение элемента: кнопка 'Зарегистрироваться' окна регистрации Физического лица")
    def get_registration_button(self):
        return self.find_element(self._registration_button)

    @allure.step("Нахождение элемента: Получение текста об ошибке при попытке зарегистрироваться через окно регистрации Физического лица")
    def get_error_message(self):
        return self.find_element(self._error_message).text

    @allure.step('Нахождение элемента: Получение текста об ошибке при попытке зарегистрироваться с пустым полем "Имя"')
    def get_error_message_missing_name(self):
        return self.find_element(self._error_message_missing_name).text

    @allure.step('Нахождение элемента: Получение текста об ошибке при попытке зарегистрироваться с пустым полем "Фамилия"')
    def get_error_message_missing_surname(self):
        return self.find_element(self._error_message_missing_surname).text

    @allure.step('Нахождение элемента: Получение текста об ошибке при попытке зарегистрироваться с пустым полем "Пароль"')
    def get_error_message_missing_password(self):
        return self.find_element(self._error_message_missing_password).text

    @allure.step('Нахождение элемента: Получение текста об ошибке при попытке зарегистрироваться с пустым полем "Номер телефона"')
    def get_error_message_missing_phone(self):
        return self.find_element(self._error_message_missing_phone).text

    @allure.step('Нахождение элемента: Получение текста об ошибке при попытке зарегистрироваться с пустым полем "Электронная почта"')
    def get_error_message_missing_email(self):
        return self.find_element(self._error_message_missing_email).text


