from selenium.webdriver.common.by import By


class YaSeleniumHelper:

    def __init__(self, app):
        """
        Инициализация драйвера и приложения.
        :param app:
        """
        self.app = app
        self.driver = self.app.driver

    def by_id(self, id_tag):
        """
        Найти элемент на web-странице по его id.
        :param id_tag:
        :return:
        """
        return self.driver.find_element(By.ID, id_tag)

    def by_name(self, name):
        """
        Найти элемент на web-странице по его имени.
        :param name:
        :return:
        """
        return self.driver.find_element(By.NAME, name)

    def by_css(self, css_selector):
        """
        Найти элемент на web-странице по его css_selector.
        :param css_selector:
        :return:
        """
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def by_xpath(self, xpath):
        """
        Найти элемент на web-странице по его xpath.
        :param xpath:
        :return:
        """
        return self.driver.find_element(By.XPATH, xpath)

    def by_linktext(self, linktext):
        """
        Найти элемент на web-странице по тексту его ссылки.
        :param linktext:
        :return:
        """
        return self.driver.find_element(By.LINK_TEXT, linktext)

    def by_partial_linktext(self, part):
        """
        Найти элемент на web-странице по частичному тексту его ссылки.
        :param part:
        :return:
        """
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, part)

    def by_tagname(self, tagname):
        """
        Найти элемент на web-странице по названию его тега.
        :param tagname:
        :return:
        """
        return self.driver.find_element(By.TAG_NAME, tagname)

    def by_classname(self, classname):
        """
        Найти элемент на web-странице по его имени класса.
        :param classname:
        :return:
        """
        return self.driver.find_element(By.CLASS_NAME, classname)

    def element_click(self, element):
        """
        Кликнуть на выбранный элемент.
        :param element:
        :return:
        """
        element.click()

    def element_send_keys(self, element, text):
        """
        Написать текст в выбранном поле.
        :param element:
        :param text:
        :return:
        """
        element.send_keys(text)

    def element_submit(self, element):
        """
        Нажать на элемент.
        :param element:
        :return:
        """
        element.submit()

    def element_get_text(self, element):
        """
        Получить текст элемента.
        :param element:
        :return:
        """
        return element.text

    def element_get_attribute(self, element, value):
        """
        Получить атрибут элемента.
        :param element:
        :param value:
        :return:
        """
        return element.get_attribute(value)

    def element_clear(self, element):
        """
        Очистить поле.
        :param element:
        :return:
        """
        element.clear()

    def get_url(self):
        """
        Получить в виде строки текущий URL страницы.
        :return:
        """
        return str(self.driver.current_url)
