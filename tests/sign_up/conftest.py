import pytest
from selenium.webdriver.common.alert import Alert
from data import credentials_admin

from constants import *
from selenium.webdriver.common.action_chains import ActionChains

from pages.users_admin_page import UsersAdminPage
from pages.sign_up_page import SignUpPage
from faker import Faker


@pytest.fixture(scope='function')
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    driver.get(MAIN_PAGE_PROD_URL)
    return sign_up_page

@pytest.fixture(scope='function')
def admin_page(driver):
    admin_page = UsersAdminPage(driver)
    url = "https://" + credentials_admin['username_admin'] + ":" + credentials_admin['password_admin'] + \
          "@" + credentials_admin['url_admin']
    driver.get(url)
    return admin_page

@pytest.fixture(scope='function')
def open_sign_up_window(driver, sign_up_page):
    """
    Осуществляет переход с главной страницы на окно регистрации
    """
    sign_up_page.get_main_page_profile_icon().click()
    action = ActionChains(driver)
    sign_up_button = sign_up_page.element_is_clickable(sign_up_page._main_page_sign_up_button)
    action.move_to_element(sign_up_button).click().perform()

def create_user(name, surname, password, phone, email, club_card_number):
    sign_up_page.get_name_field().send_keys(name)
    sign_up_page.get_surname_field().send_keys(surname)
    sign_up_page.get_password_field().send_keys(password)
    sign_up_page.get_phone_field().send_keys(phone)
    sign_up_page.get_email_field().send_keys(email)
    sign_up_page.get_club_card_number_field().send_keys(club_card_number)

def delete_user(driver, name_surname):
    admin_page.get_admin_page_search_field().send_keys(name_surname)
    admin_page.get_admin_page_search_submit_button().click()
    try:
        # Find all elements that match the selector
        checkboxes = admin_page.get_user_admin_page_checkbox()

        # Click the first checkbox if it exists
        if checkboxes:
            checkboxes[0].click()
        else:
            pytest.fail("No checkboxes found matching the selector")
    except Exception as e:
        pytest.fail(f"Failed to click the checkbox: {e}")
    assert checkboxes[0].is_selected()

    # DELETING:
    admin_page.get_admin_page_open_drop_down().click()
    admin_page.get_admin_page_drop_down_delete_option().click()
    admin_page.get_admin_page_apply_button().click()

    # Switch to the confirmation dialog
    alert = Alert(driver)

    # Accept the confirmation (clicking the "OK" button)
    alert.accept()

@pytest.fixture(scope='function')
def user_management(driver):
    fake = Faker('ru_RU')  # Create a Faker instance for Russian data

    user_data = {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "email": fake.email(),
        "phone": '9' + str(fake.random_int(min=100000000, max=999999999)),
        "password": fake.password(),
        "club_card_number": str(fake.random_int(min=100000000000, max=999999999999))
    }

    name_surname = user_data["name" + " " + "surname"]  # Unique identifier of user

    # Create a user
    create_user(user_data["password"], user_data["name"], user_data["surname"],
                user_data["email"], user_data["phone"], user_data["club_card_number"])

    # yield user_data
    #
    # # Delete the user after the test
    # delete_user(name_surname)