import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def test_show_pet_friends():
   #Проверка карточек питомцев

   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(5)

   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys(valid_email)

   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.current_url == 'http://petfriends1.herokuapp.com/all_pets'

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')

   assert names[0].text != ''
   # Ищем на странице все фотографии, имена, породу (вид) и возраст питомцев:
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ',' in descriptions[i].text
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
