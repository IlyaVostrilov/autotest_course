# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
from datetime import datetime


# Открываем окно хрома настежь
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Вход на сайт и авторизация
    driver.get('https://fix-online.sbis.ru/')
    sleep(8)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('kudas', Keys.ENTER)
    assert login.get_attribute('value') == 'kudas'
    sleep(2)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('a1s1d1f1g1', Keys.ENTER)
    sleep(2)

    # Открываем реестр Контакты
    driver.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(10)
    assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs', 'Неверный адрес сайта'

    # Создаём и отправляем сообщение себе
    create = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    sleep(3)
    create.click()
    sleep(15)
    search = driver.find_element(By.CSS_SELECTOR,
                                 '.addressee-selector-popup__browser-searchWidth '
                                 '.controls-Search__nativeField_caretEmpty')
    search.send_keys('Кудашов Алексей Николаевич')
    sleep(5)
    result = driver.find_elements(By.CSS_SELECTOR, '.msg-addressee-item')
    result[0].click()
    sleep(2)

    btr = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    message = f'Автосообщение {datetime.now().strftime("%d.%m %H:%M:%S")}'
    btr.send_keys(message, Keys.CONTROL + Keys.ENTER)
    sleep(2)

    # Ищем сообщение в списке отправленных
    sent = driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text p')
    assert sent[0].text == message, 'Сообщение не найдено'
    sleep(2)

    # Удаляем отправленное сообщение
    action_chains = ActionChains(driver)
    action_chains.move_to_element(sent[0])
    action_chains.context_click(sent[0])
    action_chains.perform()
    sleep(2)
    delete = driver.find_element(By.CSS_SELECTOR, '.controls-Menu__row [title="Перенести в удаленные"]')
    delete.click()
    sleep(2)

    # Проверяем, что сообщение удалено
    assert driver.find_elements(By.CSS_SELECTOR, '.msg-entity-text p')[0].text != message, 'Сообщение не удалено'
    print('Тест завершён успешно')

finally:
    driver.quit()
