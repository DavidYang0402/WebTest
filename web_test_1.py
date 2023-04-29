# import time as tm
# # from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# PATH = "D:\webchromedriver\chromedriver.exe"
# driver = webdriver.Chrome(options=options)

# driver.get("https://flipclass.stust.edu.tw/")
# driver.implicitly_wait(2)

# account = driver.find_element("name", "account").send_keys("4a9g0908")
# password = driver.find_element("name", "password").send_keys(
#     "Yangzhejia0402" + Keys.ENTER)


# def isElementExist(element):  # def isElementExist(self,element):
#     xoLogin = True
#     browser = driver
#     try:
#         browser.find_element(By.XPATH, element)
#         return xoLogin
#     except:
#         xoLogin = False
#         return xoLogin


# xoLogin = isElementExist("//a[@class='btn  btn-primary kickOtherBtn']")
# if xoLogin:
#     driver.find_element(
#         By.XPATH, "//a[@class='btn  btn-primary kickOtherBtn']").send_keys(Keys.ENTER)
# tm.sleep(2)

# driver.get('https://flipclass.stust.edu.tw/course/homework/70277')
# tm.sleep(2)

# driver.find_element(
#     By.XPATH, "//a[@class='btn  btn btn-primary']").send_keys(Keys.ENTER)
# tm.sleep(2)

# # --------------------iframe 切換------------------------
# # /homework/editReport/?homeworkId=70277&_lock=homeworkId&ajaxAuth=86d1d3d9e5f0b97adea0da87991e6f8c&fs_no_foot_js=1
# iframe1 = driver.find_element(By.CLASS_NAME, 'fs-modal-iframe')
# driver.switch_to.frame(iframe1)

# iframe2 = driver.find_element(By.XPATH, "//div/iframe[@class='cke_wysiwyg_frame cke_reset']")
# driver.switch_to.frame(iframe2)

# # --------------填寫區---------------
# textArea = driver.find_element(By.CSS_SELECTOR, 'div')
# driver.execute_script("arguments[0].innerHTML = '4A9G0908 楊哲家'", textArea)

# switchFrame1 = driver.switch_to.parent_frame()


# btn1 = driver.find_element(By.XPATH, "//div/button[@class='btn btn-default ']")
# btn1.click()

# # ---------------上傳檔案---------------
# inFile = driver.find_element(By.XPATH, "//input[@type='file']")
# file_path = "D:/WebTest/web_test_1.py"
# inFile.send_keys(file_path)
# tm.sleep(3)

# # --------關閉上傳頁面---------
# closeinFile = driver.find_element(
#     By.XPATH, "//div/button[@class='btn btn-primary btn-xs close-btn']")
# closeinFile.click()

# #---------------繳交---------------
# handIn = driver.find_element(By.XPATH, "//div/button[@class='btn btn-success']")
# handIn.click()

# #----------------登出程序----------------
# closeHandIn = driver.switch_to.default_content()
# tm.sleep(3)

# check = driver.find_element(By.XPATH, "//div/div[@class='alert alert-info text-center']")
# check_content = check.text
# # if (check_content == "此作業已繳交"):
# #     print('yes')
# print(check_content)

# driver.quit()
