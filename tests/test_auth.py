import allure
from playwright.sync_api import expect
from pages.auth_page import AuthPage


@allure.epic("Ростелеком ID")
@allure.feature("Авторизация")
class TestAuthentication:

    @allure.title("Отображение формы авторизации")
    def test_auth_form_display(self, auth_page):
        page = AuthPage(auth_page)

        with allure.step("Проверить наличие основных элементов формы"):
            expect(page.username_field).to_be_visible()
            expect(page.password_field).to_be_visible()
            expect(page.login_button).to_be_visible()
            expect(page.forgot_password_link).to_be_visible()


    @allure.title("Авторизация с валидными данными")
    def test_successful_login(self, auth_page):
        """Проверка успешной авторизации с корректными данными"""
        page = AuthPage(auth_page)

        with allure.step("Ввести валидные данные для авторизации"):
            page.enter_username("jane022@mail.ru")
            page.enter_password("nw@h377MQLW2cPF")

        with allure.step("Нажать кнопку входа"):
            page.click_login()

        with allure.step("Проверить успешную авторизацию"):
            page.check_successful_login()

    @allure.title("Авторизация с невалидными данными")
    def test_invalid_login(self, auth_page):
        """Проверка отображения ошибки при неверных данных"""
        page = AuthPage(auth_page)

        with allure.step("Ввести невалидные данные"):
            page.enter_username("jane022@mail.ru")
            page.enter_password("invalid_password")

        with allure.step("Нажать кнопку входа"):
            page.click_login()

        with allure.step("Проверить отображение ошибки"):
            page.check_error_message("Неверный логин или пароль")

    @allure.title("Валидация пустых полей")
    def test_empty_fields_validation(self, auth_page):
        """Проверка валидации при пустых полях"""
        page = AuthPage(auth_page)

        with allure.step("Оставить поля пустыми и нажать кнопку входа"):
            page.click_login()

        with allure.step("Проверить отображение ошибок валидации"):
            expect(auth_page.locator('#username-meta')).to_have_text('Введите номер телефона')

    @allure.title("Переход на страницу восстановления пароля")
    def test_forgot_password_link(self, auth_page):
        """Проверка перехода на страницу восстановления пароля"""
        page = AuthPage(auth_page)

        with allure.step("Нажать ссылку 'Забыл пароль'"):
            page.click_forgot_password()

        with allure.step("Проверить переход на страницу восстановления"):
            expect(auth_page.locator('#card-title')).to_have_text('Восстановление пароля')

    @allure.title("Авторизация по email")
    def test_email_login(self, auth_page):
        """Проверка авторизации по email"""
        page = AuthPage(auth_page)

        with allure.step("Переключиться на ввод по email"):
            page.switch_to_email()

        with allure.step("Ввести email и пароль"):
            page.enter_username("jane022@mail.ru")
            page.enter_password("nw@h377MQLW2cPF")

        with allure.step("Нажать кнопку входа"):
            page.click_login()

        with allure.step("Проверить успешную авторизацию"):
            page.check_successful_login()


    @allure.title("Автоматическое переключение табов при вводе данных")
    def test_auto_tab_switching(self, auth_page):
        """Проверка автоматического переключения табов при вводе разных типов данных"""
        page = AuthPage(auth_page)

        with allure.step("Ввести номер телефона и проверить переключение на таб 'Номер'"):
            page.enter_username("+79991234567")
            expect(page.phone_tab).to_have_class("rt-tab rt-tab--small rt-tab--active")

        with allure.step("Очистить поле и ввести email"):
            page.username_field.clear()
            page.enter_username("test@example.com")
            auth_page.locator('#card-title').click()

        with allure.step("Проверить переключение на таб 'Почта'"):
            expect(page.email_tab).to_have_class("rt-tab rt-tab--small rt-tab--active")

        with allure.step("Очистить поле и ввести логин"):
            page.username_field.clear()
            page.enter_username("testuser123")
            auth_page.locator('#card-title').click()

        with allure.step("Проверить переключение на таб 'Логин'"):
            expect(page.login_tab).to_have_class("rt-tab rt-tab--small rt-tab--active")

        with allure.step("Очистить поле и ввести лицевой счет"):
            page.username_field.clear()
            page.enter_username("123456789012")
            auth_page.locator('#card-title').click()

        with allure.step("Проверить переключение на таб 'Лицевой счет'"):
            expect(page.account_tab).to_have_class("rt-tab rt-tab--small rt-tab--active")

    @allure.title("Открытие раздела Помощь")
    def test_open_help(self, auth_page):
        page = AuthPage(auth_page)
        with allure.step("Нажать ссылку 'Помощь'"):
            page.open_help()
        with allure.step("Проверить, что открылась страница помощи"):
            expect(auth_page.locator('.faq-modal__title')).to_have_text('Ваш безопасный ключ к сервисам Ростелекома')

    @allure.title("Переключение видимости пароля")
    def test_password_visibility(self, auth_page):
        page = AuthPage(auth_page)
        with allure.step("Ввести пароль"):
            page.enter_password("Secret123!")
        with allure.step("Нажать на иконку 'глаз'"):
            page.see_password()
        with allure.step("Проверить, что пароль стал видимым (type='text')"):
            expect(page.password_field).to_have_attribute("type", "text")

    @allure.title("Кнопка 'Войти' активна")
    def test_login_button_enabled(self, auth_page):
        """Проверка, что кнопка 'Войти' активна и кликабельна"""
        page = AuthPage(auth_page)

        with allure.step("Проверить, что кнопка 'Войти' видна"):
            expect(page.login_button).to_be_visible()

        with allure.step("Проверить, что кнопка не заблокирована"):
            expect(page.login_button).to_be_enabled()

        with allure.step("Проверить, что кнопка содержит правильный текст"):
            expect(page.login_button).to_contain_text("Войти")

    @allure.title("Поле пароля скрыто по умолчанию")
    def test_password_field_hidden_by_default(self, auth_page):
        """Проверка, что поле пароля скрыто по умолчанию"""
        page = AuthPage(auth_page)

        with allure.step("Проверить, что поле пароля имеет тип 'password'"):
            expect(page.password_field).to_have_attribute("type", "password")

    @allure.title("Видимость кнопки 'Забыл пароль'")
    def test_forgot_password_button_visible(self, auth_page):
        """Проверка видимости кнопки 'Забыл пароль'"""
        page = AuthPage(auth_page)

        with allure.step("Проверить, что кнопка 'Забыл пароль' видна"):
            expect(page.forgot_password_link).to_be_visible()

        with allure.step("Проверить, что кнопка содержит правильный текст"):
            expect(page.forgot_password_link).to_contain_text("Забыл пароль")

@allure.epic("Ростелеком ID")
@allure.feature("Регистрация")
class TestRegistration:

    @allure.title("Имя менее 2 символов при регистрации")
    def test_name_short_registration(self, auth_page):
        """Проверка валидации имени при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию короткого имени"):
            page.enter_first_name("А")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error")).to_contain_text(
                "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")

    @allure.title("Имя более 30 символов при регистрации")
    def test_name_long_registration(self, auth_page):
        """Проверка валидации имени при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию короткого имени"):
            page.enter_first_name("Аролщщдщщщщщлщлщзлщзлщлщжлжлжлжлжщдлшщ")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error")).to_contain_text(
                "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")


    @allure.title("Фамилия менее 2 символов при регистрации")
    def test_lastname_short_registration(self, auth_page):
        """Проверка валидации фамилии при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию короткой фамилии"):
            page.enter_last_name("И")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error")).to_contain_text(
                "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")

    @allure.title("Фамилия более 30 символов при регистрации")
    def test_lastname_long_registration(self, auth_page):
        """Проверка валидации фамилии при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию короткой фамилии"):
            page.enter_last_name("Иеенененененененененененененененн")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error")).to_contain_text(
                "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")


    @allure.title("Email без домена при регистрации")
    def test_email_validation_registration(self, auth_page):
        """Проверка валидации email при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию некорректного email"):
            page.enter_email_or_phone("invalid-email")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error")).to_contain_text(
                "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")


    @allure.title("Короткий номер телефона при регистрации")
    def test_phone_short_registration(self, auth_page):
        """Проверка валидации телефона при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию короткого номера"):
            page.enter_email_or_phone("123")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error")).to_contain_text("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru")

    @allure.title("Короткий пароль при регистрации")
    def test_password_short_registration(self, auth_page):
        """Проверка валидации телефона при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Проверить валидацию короткого номера"):
            page.enter_password("123")
            page.click_register()
            expect(auth_page.locator(".rt-input-container--error").nth(4)).to_contain_text(
                "Длина пароля должна быть не менее 8 символов")


    @allure.title("Дублирование email при регистрации")
    def test_duplicate_email_registration(self, auth_page):
        """Проверка обработки дублирования email при регистрации"""
        page = AuthPage(auth_page)

        with allure.step("Перейти на страницу регистрации"):
            page.click_register_link()

        with allure.step("Заполнить форму регистрации с существующим email"):
            page.enter_first_name("Анна")
            page.enter_last_name("Иванова")
            page.enter_region()
            page.enter_email_or_phone("jane022@mail.ru")
            page.enter_password("ValidPass123")
            page.enter_confirm_password("ValidPass123")
            page.click_register()

        with allure.step("Проверить отображение предупреждения"):
            expect(auth_page.locator("h2.card-modal__title")).to_have_text('Учётная запись уже существует')
