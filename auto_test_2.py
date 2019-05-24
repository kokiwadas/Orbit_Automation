import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):

    def test_demo_accounts(self):
        driver = webdriver.Chrome(executable_path=r'\Test\chromedriver.exe')
        driver.get('http://demo.eurobank.pl/konta.html')
        title = driver.title
        print(title)
        assert title == 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont'
        driver.quit()
