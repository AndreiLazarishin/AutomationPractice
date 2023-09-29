from constants.start_page import StartPageConsts
from pages.base_page import BasePage

from pages.utils import log_decorator, rand_str


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts

    def close_google_ads(self):
        """Close the Google Ads"""
        self.click(self.constants.TOOLS_QA_XPATH)
        self.driver.execute_script("window.scrollTo(0, 120)")

    def open_elements_tree(self):
        """Open the Elements tree"""
        self.close_google_ads()
        self.click(xpath=self.constants.ELEMENTS_CARD_XPATH)

    def open_text_box_section(self):
        """Open the Text box section"""
        self.open_elements_tree()
        self.click(xpath=self.constants.TEXT_BOX_SECTION_XPATH)

    def open_check_box_section(self):
        """Open the Check box section"""
        self.open_elements_tree()
        self.click(xpath=self.constants.CHECK_BOX_SECTION_XPATH)

    @log_decorator
    def fill_text_box(self, text_box):
        """Fill the input fields"""
        self.driver.execute_script("window.scrollTo(0, 120)")
        self.fill_field(xpath=self.constants.TEXT_BOX_FULL_NAME_XPATH, value=text_box.full_name)
        self.fill_field(xpath=self.constants.EMAIL_INPUT_FIELD_XPATH, value=text_box.email)
        self.fill_field(xpath=self.constants.CURRENT_ADDRESS_FIELD_XPATH, value=text_box.cur_address)
        self.fill_field(xpath=self.constants.PERMANENT_ADDRESS_FIELD_XPATH, value=text_box.per_address)
        self.click(self.constants.SUBMIT_BUTTON_XPATH)

    @log_decorator
    def fill_email(self):
        """Fill random str into email field"""
        self.fill_field(xpath=self.constants.EMAIL_INPUT_FIELD_XPATH, value=rand_str(8))
        self.click(xpath=self.constants.SUBMIT_BUTTON_XPATH)

    @log_decorator
    def verify_submit_data(self, filled_text):
        """Fill fields and submit"""
        assert filled_text in \
               self.get_element_text(xpath=self.constants.OUTPUT_AREA_XPATH.format(output_text=filled_text))
        return StartPage(self.driver)

    @log_decorator
    def verify_email_field_validation(self):
        """Verify email field validation"""
        assert self.is_exists(xpath=self.constants.EMAIL_FIELD_ERROR_XPATH)
        return StartPage(self.driver)

    @log_decorator
    def expand_whole_home_tree(self):
        """Expand whole Home tree"""
        self.click(self.constants.EXPAND_ALL_XPATH)

    @log_decorator
    def pick_public(self):
        """Select Public"""
        self.expand_whole_home_tree()
        self.click(self.constants.PUBLIC_XPATH)

    @log_decorator
    def check_public_selected(self):
        """Verify that Public is Selected"""
        assert 'public' in self.get_element_text(xpath=self.constants.RESULT_XPATH)

    @log_decorator
    def pick_excel_file(self):
        """Select Excel file"""
        self.expand_whole_home_tree()
        self.driver.execute_script("window.scrollTo(0, 240)")
        self.click(self.constants.EXCEL_FILE_XPATH)

    @log_decorator
    def excel_file_selected(self):
        """Verify that Excel file selected"""
        assert 'excelFile' in self.get_element_text(xpath=self.constants.RESULT_XPATH)

    def open_radio_button_section(self):
        """Open the Radio Button section"""
        self.open_elements_tree()
        self.click(xpath=self.constants.CHECK_BOX_SECTION_XPATH)
