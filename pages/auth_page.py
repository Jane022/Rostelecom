from playwright.sync_api import Page, expect
import allure


class AuthPage:
    """Класс для работы со страницей авторизации Ростелеком ID"""

    def __init__(self, page: Page):
        self.page = page

        # Локаторы основных элементов
        self.username_field = page.locator("#username")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#kc-login")
        self.forgot_password_link = page.locator("#forgot_password")

        # Локаторы табов для разных типов авторизации
        self.phone_tab = page.locator("#t-btn-tab-phone")
        self.email_tab = page.locator("#t-btn-tab-mail")
        self.login_tab = page.locator("#t-btn-tab-login")
        self.account_tab = page.locator("#t-btn-tab-ls")

        # Локаторы для восстановления пароля
        self.reset_button = page.locator("#reset")

        # Локаторы сообщений
        self.error_message = page.locator("#form-error-message")
        self.info_message = page.locator(".alert-info")
        self.validation_errors = page.locator(".input-error")

        self.help_link = page.locator('.faq-modal-tip__btn')
        self.see_pass = page.locator('.rt-input__eye')

    @allure.step("Ввести логин/телефон/email")
    def enter_username(self, username: str):
        """Ввод логина, телефона или email"""
        self.username_field.fill(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str):
        """Ввод пароля"""
        self.password_field.fill(password)

    @allure.step("Нажать кнопку Войти")
    def click_login(self):
        """Нажатие кнопки входа"""
        self.login_button.click()

    @allure.step("Переключиться на авторизацию по email")
    def switch_to_email(self):
        """Переключение на таб авторизации по email"""
        self.email_tab.click()

    @allure.step("Нажать ссылку Забыл пароль")
    def click_forgot_password(self):
        """Нажатие ссылки восстановления пароля"""
        self.forgot_password_link.click()

    @allure.step("Проверить отображение ошибки")
    def check_error_message(self, expected_text: str):
        """Проверка отображения сообщения об ошибке"""
        expect(self.error_message).to_contain_text(expected_text)

    @allure.step("Проверить успешную авторизацию")
    def check_successful_login(self):
        """Проверка успешной авторизации"""
        expect(self.page).to_have_url("https://b2c.passport.rt.ru/account_b2c/page")


    # Методы для восстановления пароля

    @allure.step("Ввести подтверждение пароля")
    def enter_confirm_password(self, password: str):
        """Ввод подтверждения пароля"""
        self.page.locator("#password-confirm").fill(password)

    # Методы для регистрации
    @allure.step("Нажать ссылку Зарегистрироваться")
    def click_register_link(self):
        """Нажатие ссылки регистрации"""
        self.page.locator("#kc-register").click()

    @allure.step("Выбрать регион")
    def enter_region(self):
        self.page.locator('.rt-input__action').nth(2).click()
        self.page.locator('.rt-select__list-item').first.click()

    @allure.step("Ввести имя")
    def enter_first_name(self, first_name: str):
        """Ввод имени при регистрации"""
        self.page.locator("//input[@name='firstName']").fill(first_name)

    @allure.step("Ввести фамилию")
    def enter_last_name(self, last_name: str):
        """Ввод фамилии при регистрации"""
        self.page.locator("//input[@name='lastName']").fill(last_name)

    @allure.step("Ввести email или телефон")
    def enter_email_or_phone(self, email: str):
        """Ввод email при регистрации"""
        self.page.locator("#address").fill(email)


    @allure.step("Нажать кнопку Зарегистрироваться")
    def click_register(self):
        self.page.locator("//button[@name='register']").click()

    @allure.step("Открыть раздел Помощь")
    def open_help(self):
        self.help_link.click()

    @allure.step("Показать/скрыть пароль")
    def see_password(self):
        self.see_pass.click()
