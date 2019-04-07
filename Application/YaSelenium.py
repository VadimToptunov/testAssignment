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
        return self.driver.find_element(By.ID, id_tag)

    def by_name(self, name):
        return self.driver.find_element(By.NAME, name)

    def by_css(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)

    def by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def by_linktext(self, linktext):
        return self.driver.find_element(By.LINK_TEXT, linktext)

    def by_partial_linktext(self, part):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, part)

    def by_tagname(self, tagname):
        return self.driver.find_element(By.TAG_NAME, tagname)

    def by_classname(self, classname):
        return self.driver.find_element(By.CLASS_NAME, classname)

    def element_click(self, element):
        element.click()

    def element_send_keys(self, element, text):
        element.send_keys(text)

    def element_submit(self, element):
        element.submit()

    def element_get_text(self, element):
        return element.text

    def element_get_attribute(self, element, value):
        return element.get_attribute(value)

    def element_clear(self, element):
        element.clear()

    def get_url(self):
        return str(self.driver.current_url)
