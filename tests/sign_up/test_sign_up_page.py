from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By


@allure.epic("Sign Up Physical User")
class TestSignUp:

    @allure.title("Регистрация нового пользователя (физическое лицо)")
    @pytest.mark.smoke_test
    def test_positive_registration_of_new_physical_user_smoke(self, driver, sign_up_page):
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_name_field().send_keys("Ivan")
        sign_up_page.get_surname_field().send_keys("Петров")
        sign_up_page.get_password_field().send_keys("rhfbgvu@@11")
        sign_up_page.get_phone_field().send_keys("9889990999")
        sign_up_page.get_email_field().send_keys("testtq@uoowwyjg.tr")
        sign_up_page.get_club_card_number_field().send_keys("111111111267")
        sleep(1)
        sign_up_page.get_personal_data_agreement_checkbox().click()
        sign_up_page.get_registration_button().click()
        sleep(1)
        text = driver.find_element(By.CSS_SELECTOR, ".personal-h1").text
        assert text == "Личный кабинет"
        name = "Ivan"
        actual_name =  driver.find_element(By.CSS_SELECTOR, ".personal-content .personal-left .user-name").text
        assert name == actual_name
        # TODO DELETE CREATED ACCOUNT
        #prod
        # f1shd@uyjg.tr
        # f1shd@uooyjg.tr
        # testt@uooyjg.tr
        # testt@uooyjg.tr
        # testt@uoowwyjg.tr
        # testtq@uoowwyjg.tr

    @allure.title("Отправка формы на регистрацию уже зарегистрированного пользователя (физическое лицо)")
    @pytest.mark.regression_test
    def test_negative_registration_of_existed_physical_user_regress(self, driver, sign_up_page):
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_name_field().send_keys("Ivan")
        sign_up_page.get_surname_field().send_keys("Петров")
        sign_up_page.get_password_field().send_keys("rhfbgvu@@11")
        sign_up_page.get_phone_field().send_keys("9889990999")
        sign_up_page.get_email_field().send_keys("testtq@uoowwyjg.tr")
        sign_up_page.get_club_card_number_field().send_keys("111111111267")
        sleep(1)
        sign_up_page.get_personal_data_agreement_checkbox().click()
        sign_up_page.get_registration_button().click()
        sleep(1)
        error_message = sign_up_page.get_error_message()
        assert error_message == "ОШИБКА! Пользователь с таким email уже зарегистрирован"

    @allure.title("Регистрация нового пользователя (физическое лицо) с пустыми полями")
    @pytest.mark.regression_test
    def test_negative_registration_of_physical_user_with_all_fields_empty_regress(self, driver, sign_up_page):
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_registration_button().click()
        error_message1 = sign_up_page.get_error_message_missing_name()
        error_message2 = sign_up_page.get_error_message_missing_surname()
        error_message3 = sign_up_page.get_error_message_missing_password()
        error_message4 = sign_up_page.get_error_message_missing_phone()
        error_message5 = sign_up_page.get_error_message_missing_email()
        expected_error_message = "Необходимо заполнить данное поле"
        assert expected_error_message == error_message1 == error_message2 == error_message3 == error_message4 == error_message5