class Locators:
    username_input_name_locator = 'USER_LOGIN'  # Name of element
    password_input_name_locator = 'USER_PASSWORD'  # Name of element
    email_input_name_locator = 'USER_EMAIL'  # Name of element
    login_btn_xpath_locator = '//*[@class="custom-btn custom-btn--style-2"][@name="Login"]'  # x-path locator
    href_exit_xpath_locator = '//A[@class="__account"][@href="?logout=yes"][text()="выйти"]'
    error_message_xpath_locator = '//font[@class="errortext"]'
    forgot_your_password_xpath_locator = '//A[@class="color_tmp"][@href="/personal/profile/index.php?forgot_password=yes"][text()="Забыли свой пароль?"]'
