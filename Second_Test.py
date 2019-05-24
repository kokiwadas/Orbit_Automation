import unittest
from selenium import webdriver
from auto_test_1 import MainTests

test1 = MainTests()
test1.test_demo_login('http://demo.eurobank.pl/logowanie_etap_1.html', 'Eurobank - Bankowość Internetowa - Logowanie')


