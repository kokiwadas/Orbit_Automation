from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'\Test\chromedriver.exe')
# driver.get('http://demo.eurobank.pl/logowanie_etap_1.html')
driver.get('https://www.copypastecharacter.com')
title = driver.title

print(title)

# assert title == 'Eurobank - Bankowość Internetowa - Logowanie'
assert title == '✿ Our favorite set — CopyPasteCharacter.com'
driver.quit()
