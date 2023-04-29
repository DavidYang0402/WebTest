import time as tm
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class FlipClassTest(unittest.TestCase):
    def setUp(self):
        self._driver = webdriver.Chrome()

    def test(self):
        browser = self._driver
        browser.get("https://flipclass.stust.edu.tw/")
        browser.implicitly_wait(2)

        account = browser.find_element("name", "account").send_keys("School id")
        password = browser.find_element("name", "password").send_keys(
            "You Password" + Keys.ENTER)

        def isElementExist(self, element):  # def isElementExist(self,element):
            xoLogin = True
            try:
                browser.find_element(By.XPATH, element)
                return xoLogin
            except:
                xoLogin = False
                return xoLogin

        xoLogin = isElementExist(
            self, "//a[@class='btn  btn-primary kickOtherBtn']")

        if xoLogin:
            browser.find_element(
                By.XPATH, "//a[@class='btn  btn-primary kickOtherBtn']").send_keys(Keys.ENTER)
        tm.sleep(2)

        browser.get('https://flipclass.stust.edu.tw/course/homework/70277')
        tm.sleep(2)

        browser.find_element(
            By.XPATH, "//a[@class='btn  btn btn-primary']").send_keys(Keys.ENTER)
        tm.sleep(2)

        # --------------------iframe 切換------------------------
        iframe1 = browser.find_element(By.CLASS_NAME, 'fs-modal-iframe')
        browser.switch_to.frame(iframe1)

        iframe2 = browser.find_element(
            By.XPATH, "//div/iframe[@class='cke_wysiwyg_frame cke_reset']")
        browser.switch_to.frame(iframe2)

        # --------------填寫區---------------
        textArea = browser.find_element(By.CSS_SELECTOR, 'div')
        browser.execute_script(
            "arguments[0].innerHTML = 'School_ID Your_Name'", textArea)

        switchFrame1 = browser.switch_to.parent_frame()

        btn1 = browser.find_element(
            By.XPATH, "//div/button[@class='btn btn-default ']")
        btn1.click()

        # ---------------上傳檔案---------------
        inFile = browser.find_element(By.XPATH, "//input[@type='file']")
        file_path = "D:/WebTest/4a9g0908_web_test.py"
        inFile.send_keys(file_path)
        tm.sleep(3)

        # --------關閉上傳頁面---------
        closeinFile = browser.find_element(
            By.XPATH, "//div/button[@class='btn btn-primary btn-xs close-btn']")
        closeinFile.click()

        # ---------------繳交---------------
        handIn = browser.find_element(
            By.XPATH, "//div/button[@class='btn btn-success']")
        handIn.click()
        tm.sleep(2)

        # ----------------登出程序---------------
        browser.switch_to.default_content()
        tm.sleep(2)
        # ----------------------------------------------------------------

        check = browser.find_element(By.XPATH, "//div/div[@class='alert alert-info text-center']")
        check_content = check.text
        
        self.assertEqual(check_content, "此作業已繳交 收回作業")

    def tearDown(self):
        '''self._driver.quit()'''


if __name__ == '__main__':
    unittest.main()
