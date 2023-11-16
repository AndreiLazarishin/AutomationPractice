import logging

from pages.utils import TextBox, WebTable

log = logging.getLogger(__name__)


class TestStartPage:

    def test_verify_email_field_validation(self, start_page):
        start_page.open_text_box_section()
        start_page.fill_email()
        start_page.verify_email_field_validation()

    def test_fill_text_box_and_submit(self, start_page):
        start_page.open_text_box_section()
        text_box = TextBox()
        text_box.fill_default()
        start_page.fill_text_box(text_box)
        start_page.verify_submit_data(text_box.email)

    def test_pick_documents_public_office_option(self, start_page):
        start_page.open_check_box_section()
        start_page.pick_public()
        start_page.verify_public_selected()

    def test_pick_downloads_excel_file(self, start_page):
        start_page.open_check_box_section()
        start_page.pick_excel_file()
        start_page.verify_excel_file_selected()

    def test_pick_impressive_radio(self, start_page):
        start_page.open_radio_button_section()
        start_page.pick_impressive_radio()
        start_page.verify_impressive_button_selected()

    def test_verify_button_disabled(self, start_page):
        start_page.open_radio_button_section()
        start_page.verify_no_radio_button_disabled()

    def test_add_new_record_2_web_table(self, start_page):
        start_page.open_web_tables_section()
        web_table = WebTable()
        web_table.fill_default()
        start_page.add_random_2_web_table(web_table)
        start_page.verify_web_table_record_added(web_table.department)

    def test_search_added_record_in_web_table(self, start_page, web_table_record):
        start_page.open_web_tables_section()
        start_page.add_constant_record_2_web_table(web_table_record)
        start_page.search_in_web_table(web_table_record['first_name'])
        start_page.verify_successful_search(web_table_record['first_name'])
