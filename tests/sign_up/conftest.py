from time import sleep

import pytest
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

from data.credentials_admin import credentials_admin
from pages.sign_up_page import SignUpPage
from pages.users_admin_page import UsersAdminPage


@pytest.fixture(scope='function')
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    driver.get(credentials_admin['url_test2'])
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

@pytest.fixture(scope='function')
def name():
    fake = Faker('ru_RU')
    return fake.first_name()

@pytest.fixture(scope='function')
def surname():
    fake = Faker('ru_RU')
    return fake.last_name()

@pytest.fixture(scope='function')
def password():
    fake = Faker('ru_RU')
    return fake.password()

@pytest.fixture(scope='function')
def club_card_number():
    fake = Faker('ru_RU')
    return str(fake.random_int(min=100000000000, max=999999999999))

@pytest.fixture(scope='function')
def email():
    fake = Faker('ru_RU')
    return fake.email()

@pytest.fixture(scope='function')
def phone():
    fake = Faker('ru_RU')
    phone_number = '9' + str(fake.random_int(min=100000000, max=999999999))
    return phone_number

def create_user(name, surname, password, email, phone, sign_up_page):
    username = name
    sign_up_page.get_name_field().send_keys(username)
    sign_up_page.get_surname_field().send_keys(surname)
    sign_up_page.get_password_field().send_keys(password)
    sign_up_page.get_phone_field().send_keys(phone)
    sign_up_page.get_email_field().send_keys(email)
    # sign_up_page.get_club_card_number_field().send_keys(club_card_number)

def delete_user(driver, name, surname):
    keyword = name + " " + surname
    admin_page.get_admin_page_search_field().send_keys(keyword)
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
def user_management(driver, name, surname, password, email, phone, sign_up_page, admin_page):
    create_user(name, surname, password, email, phone, sign_up_page)
    sleep(10)

    yield

    delete_user(driver, name, surname, admin_page)
