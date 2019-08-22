from yahoo_transit_auto import YahooPositiveRun
from login_error_auto import LoginNegativeRun
import test_py_pd

# Class name of your library must be same as filename.
class robot_library:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        pass

    def test_raise_fail(self):
        raise Exception("error")

    def run_positive_test_case_yahoo_transit(self):
        hello_auto = YahooPositiveRun()

        try:
            hello_auto.move_to_url()
            input_data_path = hello_auto.common.config.INPUT_PATH_DATA
            csv_data = hello_auto.common.read_csv_dataset(input_data_path)

            for csv_item in csv_data:
                hello_auto.initialize_data_frame(csv_item)
                hello_auto.input_multiple_items_route(csv_item)
                hello_auto.common.wait_presence(sec=30, Identifier='//*[@id="srch_top"]/dd/form/fieldset/p/input',
                                                selector='xpath')
                hello_auto.route_pass_info(csv_item)
                hello_auto.move_to_url()

        except Exception as e:
            print("Error", e)
            raise Exception(e) # if not using raise, it can not make fail in robot report.
        finally:
            hello_auto.teardown()

    def run_negative_test_case_login_error(self):
        hello_auto = LoginNegativeRun()

        try:
            hello_auto.initialize_data_frame()
            hello_auto.move_to_login_page()
            hello_auto.negative_try_login()

        except Exception as e:
            print("Error", e)
            raise Exception(e)  # if not using raise, it can not make fail in robot report.
        finally:
            hello_auto.teardown()

    def test_py_panda(self):
        try:
            test_py_pd
        except Exception as e:
            print("Error", e)