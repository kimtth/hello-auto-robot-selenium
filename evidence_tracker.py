import pandas as pd
import common_setting as common
from selenium.webdriver.common.by import By


class EvidenceTracker:

    def initialize_evidence_cabinet(self, df, index_data, column_data):
        if df.empty:
            df = pd.DataFrame(columns=column_data, index=index_data)
        else:
            df2 = pd.DataFrame(columns=column_data, index=index_data)
            df = df.append(df2) # n_df.append(df, ignore_index=True) X / n_df = n_df.append(df, ignore_index=True) OK
        return df

    def append_evidence_to_cabinet(self, data_frame, value_data):
        data_frame = data_frame.append(value_data)
        return data_frame

    def populate_text_from_html_yahoo(self, df, driver, identifier, output_path):
        text_str = driver.find_element(By.XPATH, identifier).text
        new_text_str = text_str.replace(",", "")
        text_str = new_text_str.replace("\n", ",")
        df.loc[df.index[-1], 'Route1_安'] = text_str

        with pd.ExcelWriter(output_path) as writer:
            df.to_excel(writer, sheet_name='Yahoo')

    def populate_text_from_html_seison(self, df, driver, identifier, output_path):
        rtn_text = driver.find_element(By.CSS_SELECTOR, identifier).text
        df.loc[df.index[-1], 'Error_MSG'] = rtn_text

        with pd.ExcelWriter(output_path) as writer:
            df.to_excel(writer, sheet_name='Saison')

    def save_data_frame_to_excel_extra_process(self, func, df, driver, identifier, output_path):
        func(df, driver, identifier, output_path)

    def save_data_frame_to_excel(self, df, driver, identifier, output_path):
        if "yahoo" in driver.current_url:
            self.save_data_frame_to_excel_extra_process(self.populate_text_from_html_yahoo, df, driver, identifier, output_path)
        elif "saison" in driver.current_url:
            self.save_data_frame_to_excel_extra_process(self.populate_text_from_html_seison, df, driver, identifier, output_path)
        else:
            raise Exception(str(driver.current_url))
