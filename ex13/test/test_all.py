from ..page_objects.login_page import LoginPage
from ..page_objects.profile_page import ProfilePage


def test_successful_authorization(open_login_page, get_user_name, get_user_password):
    driver = open_login_page
    LoginPage(driver). \
        set_user_name(get_user_name). \
        set_password(get_user_password). \
        click_login()
    ProfilePage(driver).find_exit_href()


def test_user_login_incorrect(open_login_page, get_user_name_incorrect, get_user_password):
    driver = open_login_page
    LoginPage(driver). \
        set_user_name(get_user_name_incorrect). \
        set_password(get_user_password). \
        click_login(). \
        find_error_message()

def test_user_password_incorrect(open_login_page, get_user_name, get_user_password_incorrect):
    driver = open_login_page
    LoginPage(driver). \
        set_user_name(get_user_name). \
        set_password(get_user_password_incorrect). \
        click_login(). \
        find_error_message()


def test_empty_fields_in_form(open_login_page, get_user_name='', get_user_password=''):
    driver = open_login_page
    LoginPage(driver). \
        set_user_name(get_user_name). \
        set_password(get_user_password). \
        click_login(). \
        find_error_message()

def test_password_recovery(open_login_page):
    driver = open_login_page
    LoginPage(driver). \
        click_forgot_pass(). \
        find_fild_email()


