from selenium import webdriver

driver_path = 'D:\應用程式\WebDriver\chromedriver.exe'
driver = webdriver.Chrome(driver_path)

url = 'https://www.google.com.tw'
driver.get(url)

# find_element_by_id
# find_element_by_class_name
# find_element_by_name
# find_element_by_tag_name

tags = driver.find_elements_by_tag_name('input')
print(len(tags))

tags = driver.find_elements_by_name('q')
print(len(tags))
print(type(tags[0]))
print(tags[0].tag_name)

search_field = driver.find_element_by_name('q')
search_field.send_keys('NKNU') #傳送值
search_field.submit()   #提交表單

#back() 、 forward()
driver.back()

#1. 按下搜尋欄
#2. 按下Enter
#3. 提交
search_field = driver.find_element_by_name('q') #1.
search_field.send_keys('NKNU') #2.
search_field.send_keys()


#driver.quit()
