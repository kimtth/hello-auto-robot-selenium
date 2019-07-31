from yahoo_transit_auto import YahooPositiveRun
from login_error_auto import LoginNegativeRun


class RobotLibrary:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        pass

    def run_positive_test_case_yahoo_transit(self):
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

    def run_negative_test_case_login_error(self):
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
