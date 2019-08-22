import time
import pandas as pd
import common_setting as tool
from selenium.webdriver.common.by import By


class LoginNegativeRun:

    def __init__(self):
        self.common = tool.Common()
        self.driver = self.common.driver
        self.output_cab = pd.DataFrame()

    def move_to_login_page(self):
        self.driver.get(self.common.config.SP_OTONA_URL)
        self.driver.set_window_size(400, 800)
        time.sleep(2)

    def switch_to_window(self, login_page_identifier):
        # ref: stack_over_flow
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

    def initialize_data_frame(self):
        column_data = ['Error_MSG']
        index_data = []
        self.output_cab = self.common.cabinet.initialize_evidence_cabinet(self.output_cab, index_data, column_data)

    def close_alert_opened(self):
        pass

    def negative_try_login(self):
        self.driver.maximize_window()
        self.common.wait_presence(sec=30, Identifier='/html/body/header/div/div/p[1]/a/img', selector='xpath')
        self.switch_to_window("/html/body/header/div/div/p[1]/a/img")

        login_button_identifier = '//*[@id="login"]/img'
        self.common.wait_presence(sec=30, Identifier=login_button_identifier, selector='xpath')

        # 1
        self.common.wait_presence(sec=30, Identifier="// *[ @ id = \"close\"] / img", selector='xpath')
        time.sleep(3)

        self.driver.find_element(By.NAME, "txUserId").send_keys(self.common.config.ACCOUNT_ID)
        self.driver.find_element(By.XPATH, login_button_identifier).click()
        time.sleep(1)
        self.common.save_full_size_capture(self.driver, "nCase001")
        output_path = self.common.config.OUTPUT_DIRECTORY_PATH + "saison_output.xlsx"
        self.output_cab = self.common.cabinet.initialize_evidence_cabinet(self.output_cab, [0], ['Error_MSG'])
        self.common.cabinet.save_data_frame_to_excel(self.output_cab, self.driver, "#sa-cont > p:nth-child(1) > font", output_path)

        # 2
        self.driver.find_element(By.NAME, "txUserId").clear()
        self.driver.find_element(By.NAME, "txPassword").send_keys(self.common.config.ACCOUNT_PASS)
        self.driver.find_element(By.XPATH, login_button_identifier).click()
        time.sleep(1)
        self.common.save_full_size_capture(self.driver, "nCase002")
        self.output_cab = self.common.cabinet.initialize_evidence_cabinet(self.output_cab, [1], ['Error_MSG'])
        self.common.cabinet.save_data_frame_to_excel(self.output_cab, self.driver, "#sa-cont > p:nth-child(1) > font", output_path)

        # 3
        self.driver.find_element(By.NAME, "txPassword").clear()
        self.driver.find_element(By.ID, "txUserId").send_keys(self.common.config.ACCOUNT_ID)
        self.driver.find_element(By.ID, "txPassword").send_keys(self.common.config.ACCOUNT_PASS)
        self.driver.find_element(By.XPATH, login_button_identifier).click()
        time.sleep(1)
        self.common.save_full_size_capture(self.driver, "nCase003")
        self.output_cab = self.common.cabinet.initialize_evidence_cabinet(self.output_cab, [2], ['Error_MSG'])
        self.common.cabinet.save_data_frame_to_excel(self.output_cab, self.driver, "#sa-cont > p:nth-child(1) > font", output_path)

    def teardown(self):
        self.common.driver.quit() # quit is for closing all opened windows.


if __name__ == '__main__':
    hello_auto = LoginNegativeRun()

    try:
        hello_auto.initialize_data_frame()
        hello_auto.move_to_login_page()
        hello_auto.negative_try_login()

    except Exception as e:
        print("Error", e)
    finally:
        hello_auto.teardown()
