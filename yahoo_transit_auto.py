import time
import common_setting as tool
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class YahooPositiveRun:

    def __init__(self):
        self.common = tool.Common()
        self.driver = self.common.driver
        self.output_cab = pd.DataFrame()

    def move_to_url(self):
        self.driver.get(self.common.config.TRANSIT_URL)

    def initialize_data_frame(self, csv_item):
        column_data = ['Route1_安']
        index_data = [str(csv_item['from']) + '_' + str(csv_item['transit']) + '_' + str(csv_item['to'])]
        self.output_cab = self.common.cabinet.initialize_evidence_cabinet(self.output_cab, index_data, column_data)

    def input_multiple_items_route(self, csv_item):
        # self.common.wait_presence(sec=30, Identifier='searchModuleSubmit', selector='id')
        self.common.onload_completed(self.driver)

        self.driver.find_element(By.CSS_SELECTOR, "#departure .placeholder")
        self.driver.find_element(By.ID, "sfrom").send_keys(str(csv_item['from']))
        self.driver.find_element(By.CSS_SELECTOR, "#arrival .placeholder")
        self.driver.find_element(By.ID, "sto").send_keys(str(csv_item['to']))
        self.driver.find_element(By.CSS_SELECTOR, "#via01 .placeholder")
        self.driver.find_element(By.ID, "svia1").send_keys(str(csv_item['transit']))

        target = self.driver.find_element(By.ID, "sfrom")
        ActionChains(self.driver).move_to_element(target).perform()

        drop_down = self.driver.find_element(By.ID, "m")
        drop_down.find_element(By.XPATH, "//option[. = '7月']").click()
        drop_down = self.driver.find_element(By.ID, "d")
        drop_down.find_element(By.XPATH, "//option[. = '25日']").click()
        drop_down = self.driver.find_element(By.ID, "hh")
        drop_down.find_element(By.XPATH, "//option[. = '12時']").click()
        drop_down = self.driver.find_element(By.ID, "mm")
        drop_down.find_element(By.XPATH, "//option[. = '54分']").click()
        self.driver.find_element(By.ID, "tsArr").click()
        drop_down = self.driver.find_element(By.NAME, "expkind")
        drop_down.find_element(By.XPATH, "//option[. = '指定席優先']").click()
        drop_down = self.driver.find_element(By.NAME, "ws")
        drop_down.find_element(By.XPATH, "//option[. = '少し急いで']").click()
        drop_down = self.driver.find_element(By.NAME, "s")
        drop_down.find_element(By.XPATH, "//option[. = '料金が安い順']").click()
        self.driver.find_element(By.ID, "fer").click()
        self.driver.find_element(By.ID, "hbus").click()

        self.common.save_image_capture_with_scroll(self.driver, csv_item['no'])
        time.sleep(1)
        self.driver.find_element(By.ID, "searchModuleSubmit").click()

    def route_pass_info(self, csv_item):
        #self.common.wait_presence(sec=30, Identifier='//*[@id="tabflt"]/li[3]/a/span/span', selector='xpath')
        self.common.onload_completed(self.driver)

        # 安
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[1]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route01\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        # self.common.save_image_capture(self.driver, csv_item['no'])

        # Commute pass to Excel
        output_path = self.common.config.OUTPUT_DIRECTORY_PATH + "yahoo_output.xlsx"
        self.common.cabinet.save_data_frame_to_excel(self.output_cab, self.driver, "//*[@id=\"route01\"]/dl/dd[2]/div[1]/dl/dd", output_path)

        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[2]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route02\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        # self.common.save_image_capture(self.driver, csv_item['no'])
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[3]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route03\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        # self.common.save_image_capture(self.driver, csv_item['no'])
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        # 早
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > a > span:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[1]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route01\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        # self.common.save_image_capture(self.driver, csv_item['no'])
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        # Commute pass to Excel
        self.common.cabinet.save_data_frame_to_excel(self.output_cab, self.driver, "//*[@id=\"route01\"]/dl/dd[2]/div[1]/dl/dd", output_path)

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[2]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route02\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        # self.common.save_image_capture(self.driver, csv_item['no'])
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[3]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route03\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        # self.common.save_image_capture(self.driver, csv_item['no'])
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

    def wait_condition(self):
        if self.driver.find_element(By.CSS_SELECTOR, "#departure .placeholder").size() != 0:
            return True
        else:
            return False

    def teardown(self):
        self.common.driver.close()


if __name__ == '__main__':
    hello_auto = YahooPositiveRun()

    try:
        hello_auto.move_to_url()
        input_data_path = hello_auto.common.config.INPUT_PATH_DATA
        csv_data = hello_auto.common.read_csv_dataset(input_data_path)

        for csv_item in csv_data:
            hello_auto.initialize_data_frame(csv_item)
            hello_auto.input_multiple_items_route(csv_item)
            hello_auto.route_pass_info(csv_item)
            hello_auto.move_to_url()

    except Exception as e:
        print("Error", e)
    finally:
        hello_auto.teardown()

