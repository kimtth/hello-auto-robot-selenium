import configparser
import time
import csv
import os
from tkinter.filedialog import askopenfilename
import evidence_tracker
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Config:

    def __init__(self):
        config = configparser.ConfigParser()
        # filename = askopenfilename()
        # config.read(filename)
        config.read('C:/Users/Admin/PycharmProjects/demoTraning/dataset/config.ini')

        self.CHROME_DRIVER_PATH = config['PATH']['CHROME_DRIVER_PATH']
        print(self.CHROME_DRIVER_PATH)
        self.INPUT_PATH_DATA = config['PATH']['INPUT_PATH_DATA']
        self.OUTPUT_DIRECTORY_PATH = config['PATH']['OUTPUT_DIRECTORY_PATH']

        if not os.path.exists(self.OUTPUT_DIRECTORY_PATH):
            os.makedirs(self.OUTPUT_DIRECTORY_PATH)

        self.ACCOUNT_ID = config['ACCOUNT']['ACCOUNT_ID']
        self.ACCOUNT_PASS = config['ACCOUNT']['ACCOUNT_PASS']

        self.TRANSIT_URL = config['URL']['TRANSIT_URL']
        self.SP_OTONA_URL = config['URL']['SP_OTONA_URL']


class Common:

    def __init__(self):
        self.config = Config()
        self.cabinet = evidence_tracker.EvidenceTracker()

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"
        chrome_options = Options()
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(options=chrome_options, desired_capabilities=caps, executable_path=self.config.CHROME_DRIVER_PATH)
        self.driver.maximize_window()

    def onload_completed(self, driver):
        status = driver.execute_script("return document.readyState;")
        while True:
            if status == 'complete':
                break
            else:
                time.sleep(0.5)
                status = driver.execute_script("return document.readyState;")

    def save_image_capture_with_scroll(self, driver, no):
        time.sleep(0.5)
        top_position = driver.execute_script('return !window.pageYOffset')
        while True:
            if top_position:
                break
            else:
                time.sleep(0.5)
                driver.execute_script("document.documentElement.scrollTop = 0;")
                time.sleep(0.5)
                top_position = driver.execute_script('return !window.pageYOffset')

        scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        client_height = driver.execute_script("return window.innerHeight")

        while scroll_height > 0:
            file_stamp = "evidence_log_" + no + "_" + time.strftime("%Y%m%d%H%M%S") + ".png"
            driver.save_screenshot(self.config.OUTPUT_DIRECTORY_PATH + file_stamp)

            time.sleep(0.5)
            driver.execute_script("window.scrollBy(0," + str(client_height) + ")") # not working scrollTo
            time.sleep(0.5)
            scroll_height = scroll_height - client_height

    def save_full_size_capture(self, driver, no):
        time.sleep(1)
        element = driver.find_element_by_tag_name('body')
        element_png = element.screenshot_as_png

        time_str = time.strftime("%Y%m%d%H%M%S")
        file_stamp = "evidence_log_" + no + "_" + str(time_str) + ".png"
        with open(self.config.OUTPUT_DIRECTORY_PATH + file_stamp, "wb") as file:
            file.write(element_png)

    def read_csv_dataset(self, input_path):
        rtn_list = list()

        with open(input_path,  encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rtn_dictionary = dict()
                for k, v in row.items():
                    rtn_dictionary[k] = v
                rtn_list.append(rtn_dictionary)

        return rtn_list

    def save_csv_evidence(self, append_row):
        time_str = time.strftime("%Y%m%d")
        file_stamp = "evidence_log_" + str(time_str) + ".csv"

        with open(self.config.OUTPUT_DIRECTORY_PATH + file_stamp, "a+") as fd:
            fd.write(append_row)
        fd.close()

    def identifier_type_traverser(self, identifier_type):
        if identifier_type == "id":
            select_ob = By.ID
        elif identifier_type == "xpath":
            select_ob = By.XPATH
        elif identifier_type == "name":
            select_ob = By.NAME
        elif identifier_type == "tag":
            select_ob = By.TAG_NAME
        elif identifier_type == "class":
            select_ob = By.CLASS_NAME
        elif identifier_type == "css":
            select_ob = By.CSS_SELECTOR
        elif identifier_type == "link":
            select_ob = By.LINK_TEXT
        else:
            raise Exception

        return select_ob

    def wait_presence(self, **key_args):
        selector = key_args['selector']
        select_ob = self.identifier_type_traverser(selector)

        WebDriverWait(self.driver, key_args['sec']).until(
            expected_conditions.presence_of_element_located((select_ob, key_args['Identifier'])))

    def wait_for(self, condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Time waiting for {}'.format(condition_function.__name__)
        )
