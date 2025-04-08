import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestOpenBrowser:
    # Фикстура создания драйвера открытия Google Chrome
    @pytest.fixture(scope="class")
    def create_driver_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        return driver

    # Тест открытия страницы hh.ru и проверка, что находимся там
    def test_open_browser(self, create_driver_chrome):
        base_url = 'https://www.hh.ru'
        create_driver_chrome.get(base_url)
        create_driver_chrome.set_window_size(1920, 1080)
        time.sleep(5)
        header = create_driver_chrome.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[4]/div[1]/div[1]/div/div/div/div[1]/div/div/h3').text
        print(header)
        assert header == 'Найдите работу уже завтра', 'Ошибка! Страница браузера не открылась'
        print('Тест успешен! Вы находитесь на главной странице hh.ru')