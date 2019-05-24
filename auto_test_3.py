import unittest
from selenium import webdriver
import time

# class MainTests(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(executable_path=r'C:\Python\Test\chromedriver.exe')

#      def test_demo_login(self):
#          driver = self.driver
#          url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
#          driver.get(url)
#          title = driver.title
#          print(f'Actual title: {title}')
#          self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Logowanie',
#                           f'Actual title differ from expected for page url: {url}.')
#
#      def test_demo_accounts(self):
#          driver = self.driver
#          url = 'http://demo.eurobank.pl/konta.html'
#          driver.get(url)
#          title = driver.title
#          print(f'Actual title: {title}')
#          self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont',
#                           f'Actual title differ from expected for page url: {url}.')
#
#      def test_demo_pulpit(self):
#          driver = self.driver
#          url = 'http://demo.eurobank.pl/pulpit.html'
#          driver.get(url)
#          title = driver.title
#          print(f'Actual title: {title}')
#          self.assertEqual(title, 'Eurobank - Bankowość Internetowa - Pulpit',
#                           f'Actual title differ from expected for page url: {url}.')

#      @classmethod
#      def tearDownClass(cls):
#          cls.driver.quit()


class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\Python\Test\chromedriver.exe')

    # def test_demo_login(self):
    #     driver = self.driver
    #     url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
    #     driver.get(url)
    #     login_form_header_element = driver.find_element_by_xpath('//*[@id="login_form"]/h1')
    #     login_form_header_text = login_form_header_element.text
    #     self.assertEqual(login_form_header_text, "Wersja demonstracyjna serwisu eurobank online",
    #                      f'Actual title: {login_form_header_text}')

    # def test_next_button_is_disabled_when_login_input_is_empty(self):
    #     driver = self.driver
    #     url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
    #     driver.get(url)
    #     # clearing the text input field
    #     login_form_id_input_field = driver.find_element_by_xpath('//*[@id="login_id"]')
    #     login_form_id_input_field.clear()
    #     login_form_next_button = driver.find_element_by_xpath('//*[@id="login_next"]')
    #     login_form_next_button_disabled = login_form_next_button.get_attribute("disabled")
    #     self.assertEqual(login_form_next_button_disabled, 'http://demo.eurobank.pl/logowanie_etap_2.html',
    #                      f'Not enough characters in the id you have provided.')

    # def test_checking_warning_messages_when_login_input_has_less_than_8_characters(self):
    #     driver = self.driver
    #     url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
    #     driver.get(url)
    #     # finding text field
    #     login_form_id_input_field = driver.find_element_by_xpath('//*[@id="login_id"]')
    #     # clearing the text input field
    #     login_form_id_input_field.clear()
    #     # entering insufficient amount of characters
    #     login_form_id_input_field.send_keys('123456')
    #
    #     hint_button_element = driver.find_element_by_xpath(
    #         '//*[@id="login_id_container"]//*[@class="i-hint-white tooltip widget-info"]')
    #     hint_button_element.click()
    #
    #     warning_message_element = driver.find_element_by_xpath('//*[@class="error"]')
    #     warning_message_text = warning_message_element.text
    #     self.assertEqual(warning_message_text, 'identyfikator ma min. 8 znaków',
    #                      f'Actual warning message differ from expected one')

    # def test_successfull_login_action(self):
    #     driver = self.driver
    #     url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
    #     driver.get(url)
    #     # finding text field
    #     login_form_id_input_field = driver.find_element_by_xpath('//*[@id="login_id"]')
    #     # clearing the text input field
    #     login_form_id_input_field.clear()
    #     # entering the sufficient amount of characters
    #     login_form_id_input_field.send_keys('12345678')
    #     login_form_next_button = driver.find_element_by_xpath('//*[@id="login_next"]')
    #     login_form_next_button.click()
    #     time.sleep(3)
    #     login_next_button_element = driver.find_element_by_xpath('//*[@id="login_next"]')
    #     new_login_button_text = login_next_button_element.text
    #     self.assertEqual(new_login_button_text, 'zaloguj się',
    #                      f'Actual login button text {new_login_button_text}: differ from expected')

    # def test_id_reminder(self):
    #     driver = self.driver
    #     url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
    #     driver.get(url)
    #     login_form_id_rem_link = driver.find_element_by_xpath('//*[@id="ident_rem"]')
    #     login_form_id_rem_link.click()
    #     time.sleep(3)
    #     login_form_popup_message = driver.find_element_by_xpath('//*[@class="shadowbox-content contact-popup"]/div/h2')
    #     login_form_popup_message_text = login_form_popup_message.text
    #     self.assertEqual(login_form_popup_message_text, "w wersji demonstracyjnej ta funkcja jest niedostępna",
    #                      f'Actual popup message: {login_form_popup_message_text}')
    #     login_form_popup_close_button = driver.find_element_by_xpath('//*[@id="shadowbox"]/div/i')
    #     login_form_popup_close_button.click()
    #     time.sleep(3)

    def test_second_login_phase(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_2.html'
        driver.get(url)
        login_form_id_input_field = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_form_id_input_field.send_keys("12345678")
        login_form_password_input_field = driver.find_element_by_xpath('//*[@id="login_password"]')
        login_form_password_input_field.send_keys("12345678")
        login_form_login_button = driver.find_element_by_xpath('//*[@id="login_next"]')
        login_form_login_button.click()
        time.sleep(5)
        current_url = driver.current_url
        self.assertEqual(current_url, 'http://demo.eurobank.pl/pulpit.html', f'Actual URL: {current_url}')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()