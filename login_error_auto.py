import time
import common_fuction as tool
from selenium.webdriver.common.by import By


class LoginNegativeRun:

    def __init__(self):
        self.common = tool.Common()
        self.driver = self.common.driver

    def move_to_login_page(self):
        self.driver.get(self.common.config.SP_OTONA_URL)

    def switch_to_window(self, login_page_identifier):
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = self.driver.current_window_handle
        self.driver.find_element_by_xpath(login_page_identifier).click()

        sign_in_window_handle = None
        while not sign_in_window_handle:
            for handle in self.driver.window_handles:
                if handle != main_window_handle:
                    sign_in_window_handle = handle
                    break
        self.driver.switch_to.window(sign_in_window_handle)

    def negative_try_login(self):
        self.common.wait_presence(sec=30, Identifier='/html/body/header/div/div/p[1]/a/img', selector='xpath')
        self.switch_to_window("/html/body/header/div/div/p[1]/a/img")

        login_button_identifier = '//*[@id="login"]/img'
        self.common.wait_presence(sec=30, Identifier=login_button_identifier, selector='xpath')

        # 1
        self.driver.find_element(By.NAME, "txUserId").send_keys("aaaaa@cccc.xxx")
        self.driver.find_element(By.XPATH, login_button_identifier).click()
        time.sleep(2)

        # 2
        self.driver.find_element(By.NAME, "txUserId").clear()
        self.driver.find_element(By.NAME, "txPassword").send_keys("bbbbbbbbb")
        self.driver.find_element(By.XPATH, login_button_identifier).click()
        time.sleep(2)

        # 3
        self.driver.find_element(By.NAME, "txPassword").clear()
        self.driver.find_element(By.ID, "txUserId").send_keys("aaaaa@cccc.xxx")
        self.driver.find_element(By.ID, "txPassword").send_keys("bbbbbbbbb")
        self.driver.find_element(By.XPATH, login_button_identifier).click()
        time.sleep(2)

    def teardown(self):
        self.common.driver.close()


if __name__ == '__main__':
    hello_auto = LoginNegativeRun()

    try:
        hello_auto.move_to_login_page()
        hello_auto.negative_try_login()
    except Exception as e:
        print("Error", e)
    finally:
        from tkinter import messagebox

        ret = messagebox.askyesno('Bye Bye', 'Exit')
        if ret is True:
            hello_auto.teardown()
