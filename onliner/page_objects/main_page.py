from framework.base_page import BasePage
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self):
        super().__init__(self.TITLE_LOCATOR, "Все суперцены!")

    TITLE_LOCATOR = (
        By.XPATH, '//header[@class="b-main-page-blocks-header-2 cfix"]/a')
    CATALOG_TOP_BAR = '//a[contains(@class,"b-main-navigation__link")]/span[text()="{0}"]'
    CATALOG_PAGE_SECTION = '//header[@class="b-main-page-blocks-header-2 cfix"]//a[contains(text(), normalize-space("{0}"))]'

    def click_on_catalog_top_bar(self, section):
        catalog_top_bar = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, (By.XPATH, self.CATALOG_TOP_BAR.format(section)))
        catalog_top_bar.click_and_wait()

    def click_on_catalog_page_section(self, section):
        catalog_page_section = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, (By.XPATH, self.CATALOG_PAGE_SECTION.format(section)))
        catalog_page_section.click_and_wait()
