import logging

from pages.utils import TextBox

log = logging.getLogger(__name__)


class TestStartPage:

    def test_verify_email_field_validation(self, start_page):
        start_page.open_text_box_section()
        start_page.fill_email()
        start_page.verify_email_field_validation()

    def test_text_box_and_submit(self, start_page):
        start_page.open_text_box_section()
        text_box = TextBox()
        text_box.fill_default()
        start_page.fill_text_box(text_box)
        start_page.verify_submit_data(text_box.email)

    def test_pick_public_option(self, start_page):
        start_page.open_check_box_section()
        start_page.pick_public()
        start_page.check_public_selected()
