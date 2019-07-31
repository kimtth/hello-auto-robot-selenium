import pytest
import time
import common_fuction as tool
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class YahooPositiveRun:

    def __init__(self):
        self.common = tool.Common()
        self.driver = self.common.driver

    def move_to_url(self):
        self.driver.get(self.common.config.TRANSIT_URL)

    def input_multiple_items_route(self):
        self.driver.find_element(By.CSS_SELECTOR, "#departure .placeholder")
        self.driver.find_element(By.ID, "sfrom").send_keys("東京")
        self.driver.find_element(By.CSS_SELECTOR, "#arrival .placeholder")
        self.driver.find_element(By.ID, "sto").send_keys("神谷町")
        self.driver.find_element(By.CSS_SELECTOR, "#via01 .placeholder")
        self.driver.find_element(By.ID, "svia1").send_keys("有楽町")

        target = self.driver.find_element(By.ID, "sfrom")
        ActionChains(self.driver).move_to_element(target).perform()

        self.driver.find_element(By.ID, "m").click()
        drop_down = self.driver.find_element(By.ID, "m")
        drop_down.find_element(By.XPATH, "//option[. = '7月']").click()
        self.driver.find_element(By.ID, "m").click()
        self.driver.find_element(By.ID, "d").click()
        drop_down = self.driver.find_element(By.ID, "d")
        drop_down.find_element(By.XPATH, "//option[. = '25日']").click()
        self.driver.find_element(By.ID, "d").click()
        self.driver.find_element(By.ID, "hh").click()
        drop_down = self.driver.find_element(By.ID, "hh")
        drop_down.find_element(By.XPATH, "//option[. = '12時']").click()
        self.driver.find_element(By.ID, "hh").click()
        self.driver.find_element(By.ID, "mm").click()
        drop_down = self.driver.find_element(By.ID, "mm")
        drop_down.find_element(By.XPATH, "//option[. = '54分']").click()
        self.driver.find_element(By.ID, "mm").click()
        self.driver.find_element(By.ID, "tsArr").click()
        self.driver.find_element(By.NAME, "expkind").click()
        drop_down = self.driver.find_element(By.NAME, "expkind")
        drop_down.find_element(By.XPATH, "//option[. = '指定席優先']").click()
        self.driver.find_element(By.NAME, "expkind").click()
        self.driver.find_element(By.NAME, "ws").click()
        drop_down = self.driver.find_element(By.NAME, "ws")
        drop_down.find_element(By.XPATH, "//option[. = '少し急いで']").click()
        self.driver.find_element(By.NAME, "ws").click()
        self.driver.find_element(By.NAME, "s").click()
        drop_down = self.driver.find_element(By.NAME, "s")
        drop_down.find_element(By.XPATH, "//option[. = '料金が安い順']").click()
        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.ID, "fer").click()
        self.driver.find_element(By.ID, "hbus").click()
        self.driver.find_element(By.ID, "searchModuleSubmit").click()

    def route_pass_info(self):
        self.common.wait_presence(sec=30, Identifier='//*[@id="tabflt"]/li[3]/a/span/span', selector='xpath')

        # 安
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[1]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route01\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[2]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route02\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[3]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route03\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        # 早
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > a > span:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[1]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route01\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[2]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route02\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(Keys.HOME).perform()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"rsltlst\"]/li[3]/dl/dt/a").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//*[@id=\"route03\"]/dl/dd[2]/ul/li[2]/p/a/span").click()
        time.sleep(1)
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
        hello_auto.common.wait_presence(sec=30, Identifier='#departure .placeholder', selector='css')
        hello_auto.input_multiple_items_route()
        hello_auto.common.wait_presence(sec=30, Identifier='[↓]ルート1', selector='link')
        hello_auto.route_pass_info()

    except Exception as e:
        print("Error", e)
    finally:
        from tkinter import messagebox
        ret = messagebox.askyesno('Bye Bye', 'Exit')
        if ret is True:
            hello_auto.teardown()

