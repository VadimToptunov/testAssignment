import pytest
from Application.AppYa import App


@pytest.fixture(scope="session")
def ya_fixture():
    """
    Фикстура pytest, позволяющая запускать тест на Selenium WebDriver
    в пределах сессии.
    :return:
    """
    app = App()
    yield app
    app.quit()
