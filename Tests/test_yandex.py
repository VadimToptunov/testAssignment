def test_yandex_post(ya_fixture):
    """
    Предусловия: пользователь, имеющий аккаунт на почтовом любом общедоступном сервере
    электронной почты.

    Шаги воспроизведения:
        1. Открыть страницу входа веб-интерфейса почтового клиента
        2. Войти пользователем из предусловия.
        3. Создать новое письмо.
        4. Заполнить тему и тело письма (по желанию заполнить получателя).
        5. Сохранить как черновик.
        6. Перейти к черновикам.
            Ожидаемый результат: созданный черновик письма отображается в списке
            черновиков.

    :param ya_fixture:
    :return:
    """
    ya_fixture.yandex_page()
    ya_fixture.yandex.find_post()
    ya_fixture.yandex.write_credentials("login", "password")
    ya_fixture.yandex.create_new_letter()
    ya_fixture.yandex.fill_letter()
    ya_fixture.yandex.save_draft()
    ya_fixture.yandex.inspect_draft()
    ya_fixture.yandex.check_draft_presents()
