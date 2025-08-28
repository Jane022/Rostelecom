import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    """Фикстура для запуска браузера"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )
        yield browser
        browser.close()

@pytest.fixture
def context(browser: Browser):
    """Фикстура для создания контекста браузера"""
    context = browser.new_context(
        viewport={'width': 1200, 'height': 900},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
    yield context
    context.close()

@pytest.fixture
def page(context: BrowserContext):
    """Фикстура для создания страницы"""
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def auth_page(page: Page):
    """Фикстура для открытия страницы авторизации"""
    page.goto("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=48b7e9cf-75a1-454d-b50a-3f9dfd28a15e")
    return page
