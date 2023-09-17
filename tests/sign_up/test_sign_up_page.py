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
        # TODO: Postcondition: delete created user
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
        # TODO: Precondition: create user
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
        # TODO: Postcondition: delete created user

    @allure.title("Регистрация нового пользователя (физическое лицо) с пустыми полями")
    @pytest.mark.xfail(reason="Текст ошибок выводится, но не в том месте: https://trello.com/c/yujXCdJJ")
    @pytest.mark.regression_test
    def test_negative_registration_of_physical_user_with_all_fields_empty_regress(self, driver, sign_up_page):
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_registration_button().click()
        error_message1 = sign_up_page.get_error_message_wrong_name()
        error_message2 = sign_up_page.get_error_message_wrong_surname()
        error_message3 = sign_up_page.get_error_message_wrong_password()
        error_message4 = sign_up_page.get_error_message_wrong_phone()
        error_message5 = sign_up_page.get_error_message_wrong_email()
        expected_error_message = "Необходимо заполнить данное поле"
        assert expected_error_message == error_message1 == error_message2 == error_message3 == error_message4 == error_message5

    @allure.title('Регистрация нового пользователя (физ лицо) без проставления галочки в чек-боксе "Я согласен на обработку моих персональных данных"')
    @pytest.mark.xfail(reason="https://trello.com/c/2P5BbbsW")
    @pytest.mark.regression_test
    def test_negative_registration_of_physical_user_with_checkbox_off_regress(self, driver, sign_up_page):
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_name_field().send_keys("Ivan")
        sign_up_page.get_surname_field().send_keys("Петров")
        sign_up_page.get_password_field().send_keys("rhfbgvu@@11")
        sign_up_page.get_phone_field().send_keys("9889990999")
        sign_up_page.get_email_field().send_keys("testtq@uoowwyjg.tr")
        sign_up_page.get_club_card_number_field().send_keys("111111111267")
        # sign_up_page.get_personal_data_agreement_checkbox().click()
        sign_up_page.get_registration_button().click()
        # TODO ASSERTION OF ERROR MESSAGE AFTER FIXING THE BUG

    @allure.title('Регистрация нового пользователя (физ лицо) с вводом невалидных данных в поле "Пароль"')
    @pytest.mark.xfail(reason="https://trello.com/c/0BuspDgA, https://trello.com/c/oYa4lR9a")
    @pytest.mark.regression_test
    def test_negative_registration_of_physical_user_with_invalid_input_in_password_regress(self, driver, sign_up_page):
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_name_field().send_keys("Ivan")
        sign_up_page.get_surname_field().send_keys("Петров")
        sign_up_page.get_phone_field().send_keys("9889990999")
        sign_up_page.get_email_field().send_keys("testtq@uoowwyjg.tr")
        sign_up_page.get_club_card_number_field().send_keys("111111111267")
        sign_up_page.get_personal_data_agreement_checkbox().click()

        sign_up_page.get_password_field().send_keys(" ")
        sign_up_page.get_personal_data_agreement_checkbox().click()
        # TODO ASSERTION OF ERROR MESSAGE AFTER FIXING THE BUG
        sign_up_page.get_password_field().send_keys("кИрИлЛиЦа")
        sign_up_page.get_personal_data_agreement_checkbox().click()
        # TODO ASSERTION OF ERROR MESSAGE AFTER FIXING THE BUG

    @allure.title('Регистрация нового пользователя (физлицо) с введенными невалидными данными в поле "Электронная почта": "{invalid_email}", ожидаемая ошибка: "{expected_error_message}"')
    @pytest.mark.xfail(reason="https://trello.com/c/tb61Ragb")
    @pytest.mark.regression_test
    @pytest.mark.parametrize("invalid_email", [
        "орзгрз@gmail.com",
        "ivanovgmail.com",
        "ivanov@@gmail.com",
        "iva nov@gmail.co m",
        "@gmail.com",
        "ivanov@",
        "ivenovtesttt@gmailcom",
        "ivanovtest@gmail."
    ])
    def test_negative_registration_of_physical_user_invalid_input_in_mail_regress(self, driver, sign_up_page, invalid_email):
        expected_error_message = "Укажите верный email адрес"
        sign_up_page.get_main_page_profile_icon().click()
        sign_up_page.get_main_page_sign_up_button().click()
        sign_up_page.get_name_field().send_keys("TEST_NAME")
        sign_up_page.get_surname_field().send_keys("Петров")
        sign_up_page.get_password_field().send_keys("rhfbgvu@@11")
        sign_up_page.get_phone_field().send_keys("9889990999")
        sign_up_page.get_personal_data_agreement_checkbox().click()

        sign_up_page.get_email_field().send_keys(invalid_email)
        sign_up_page.get_registration_button().click()

        error_message = sign_up_page.get_error_message_wrong_email()
        assert error_message == expected_error_message

        sign_up_page.get_email_field().clear()
        sleep(1)
        # TODO: Postcondition (if test failed): delete created user / log out if account created

