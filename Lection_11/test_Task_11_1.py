# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(sbis_site)
    assert driver.current_url == 'https://sbis.ru/', 'Неверный адрес сайта'
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts_txt = 'Контакты'
    assert contacts.text == contacts_txt
    contacts.click()
    sleep(3)
    tensor_banner = driver.find_element(By.CSS_SELECTOR,
                                        '#contacts_clients [alt="Разработчик системы СБИС — компания «Тензор»"]')
    tensor_banner.click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    power = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert power.is_displayed()
    about = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content [href="/about"]')
    x = about.location_once_scrolled_into_view
    sleep(2)
    about.click()
    sleep(3)
    about_url = 'https://tensor.ru/about'
    assert driver.current_url == 'https://tensor.ru/about'
    print('Тест завершён успешно')

finally:
    driver.quit()
