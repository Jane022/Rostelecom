# Автоматизированное тестирование Ростелеком ID

Проект автоматизированного тестирования системы авторизации Ростелеком ID с использованием Playwright и pytest.

## Структура проекта

```
rostelecom/
├── conftest.py          # Конфигурация pytest и фикстуры
├── pytest.ini.py        # Настройки pytest
├── requirements.txt     # Зависимости проекта
├── README.md           # Документация
├── pages/
│   └── auth_page.py    # Page Object Model для страницы авторизации
└── tests/
    └── test_auth.py    # Тесты авторизации
```

## Установка и настройка

1. **Клонирование репозитория:**
   ```bash
   git clone <repository-url>
   cd rostelecom
   ```

2. **Создание виртуального окружения:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # или
   .venv\Scripts\activate     # Windows
   ```

3. **Установка зависимостей:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Установка браузеров Playwright:**
   ```bash
   playwright install
   ```

## Запуск тестов

### Запуск всех тестов
```bash
pytest
```
