import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем параметр --language с дефолтным значением "en"
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="choose language for tests")


# Создаем фикстуру, которая возвращает значение параметра --language
@pytest.fixture(scope="module")
def language(request):
    return request.config.getoption("--language")


# Создаем фикстуру, которая запускает браузер с указанным языком пользователя
@pytest.fixture(scope="function")
def browser(language):
    # Делаем автоинсталл драйвера. Сервис драйвера
    service = Service(ChromeDriverManager().install())
    # Создаем экземпляр опций браузера
    options = Options()
    # Добавляем опцию, которая устанавливает язык браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # Создаем экземпляр драйвера браузера
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(5)
    # Возвращаем драйвер в качестве результата фикстуры
    yield browser
    browser.quit()
