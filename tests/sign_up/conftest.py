import pytest
from constants import *
from selenium.webdriver.common.action_chains import ActionChains
from pages.sign_up_page import SignUpPage


@pytest.fixture(scope='function')
def sign_up_page(driver):
    sign_up_page = SignUpPage(driver)
    driver.get(MAIN_PAGE_PROD_URL)
    return sign_up_page


@pytest.fixture(scope='function')
def open_sign_up_window(driver, main_page):
    """
    Осуществляет переход с главной страницы на окно авторизации
    """
    main_page.get_main_page_profile_icon().click()
    action = ActionChains(driver)
    sign_up_button = main_page.element_is_clickable(main_page._main_page_sign_up_button)
    action.move_to_element(sign_up_button).click().perform()
