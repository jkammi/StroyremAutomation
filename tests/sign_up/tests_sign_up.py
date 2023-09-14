from time import sleep

import pytest
import allure


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
        sign_up_page.get_email_field().send_keys("f1shd@uyjg.tr")
        sign_up_page.get_club_card_number_field().send_keys("111111111370")
        sign_up_page.get_personal_data_agreement_checkbox().click()
        sign_up_page.get_registration_button().click()
        sleep(1000)
        # TODO ASSERTIONS
        # TODO DELETE CREATED ACCOUNT
