import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Test\chromedriver.exe')

    def test_demo_login(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/logowanie_etap_1.html')
        title = driver.title
        print(f'Actual title: {title}')
        assert title == 'Eurobank - Bankowość Internetowa - Logowanie'

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/konta.html')
        title = driver.title
        print(f'Actual title: {title}')
        assert title == 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont'

    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('http://demo.eurobank.pl/pulpit.html')
        title = driver.title
        print(f'Actual title: {title}')
        assert title == 'Eurobank - Bankowość Internetowa - Pulpit'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
