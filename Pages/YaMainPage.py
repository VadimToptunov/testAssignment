from Application.YaSelenium import YaSeleniumHelper
import random
import re
from selenium.webdriver.common.keys import Keys
import string


class YaMainPageHelper:
    def __init__(self, app):
        """
        Инициализация основных параметров: драйвера, ожидания и темы письма.
        :param app:
        """
        self.ysh = YaSeleniumHelper(app)
        self.driver = self.ysh.driver
        self.ysh.driver.implicitly_wait(10)
        self.topic = self.create_topic()

    def find_post(self):
        """
        На основной странице Яндекса найти кнопку "Войти в почту"
        и кликнуть на нее
        :return:
        """
        button = self.ysh.by_linktext("Войти в почту")
        self.ysh.element_click(button)

    def write_credentials(self, login, passw):
        """
        Ввести в поля логина и пароля данные пользователя.
        :param login:
        :param passw:
        :return:
        """
        login_field = self.ysh.by_name("login")
        self.ysh.element_send_keys(login_field, login)
        self.ysh.element_submit(login_field)
        passwd_field = self.ysh.by_name("passwd")
        self.ysh.element_send_keys(passwd_field, passw)
        self.ysh.element_submit(passwd_field)

    def create_new_letter(self):
        """
        Создать новое письмо путем нажатия кнопки "Написать" в почтовом ящике
        :return:
        """
        write_button = self.ysh.by_xpath("//*[@class='svgicon svgicon-mail--ComposeButton']")
        self.ysh.element_click(write_button)

    def fill_letter(self):
        """
        Заполнить поля письма: Кому, Тема и тело письма.
        Заполняется рандомно сгенерированным текстом.
        :return:
        """
        self.ysh.element_send_keys(self.ysh.by_name("to"), self.randomizer(6))
        topic = self.ysh.by_xpath("//*[contains(@name, 'subj-')]")
        self.ysh.element_send_keys(topic, self.topic)
        letter = self.ysh.by_xpath("//*[@role='textbox']")
        self.ysh.element_send_keys(letter, self.randomizer(212))

    def create_topic(self):
        """
        Создать рандомный текст для темы письма. По этому тексту в дальнейшем будет
        вестись проверка наличия письма в папке "Черновики"
        :return:
        """
        return self.randomizer(12)

    def save_draft(self):
        """
        Сохранить письмо в черновиках путем нажатия горячих клавиш Ctrl + S
        :return:
        """
        self.ysh.element_send_keys(self.ysh.by_tagname('body'), Keys.CONTROL + "s")

    def inspect_draft(self):
        """
        Перейти на страницу с черновиками.
        :return:
        """
        result = re.search(r'uid=\d+', self.ysh.get_url())
        uid = result.group(0)
        self.ysh.driver.get(f"https://mail.yandex.ru/?{uid}#draft")

    def check_draft_presents(self):
        """
        Проверить, что присутстсвует письмо с ранее сгенерированной темой.
        :return:
        """
        self.ysh.by_xpath(f"//*[@title='{self.topic}']")

    def randomizer(self, length):
        """
        Рандомайзер для создания текста с заданной в паораметрах длиной.
        :param length:
        :return:
        """
        return ''.join(random.choice(string.ascii_uppercase +
                string.ascii_lowercase + string.digits + string.punctuation)
                       for _ in range(length))

