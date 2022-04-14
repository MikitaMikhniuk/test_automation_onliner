from framework.base_page import BasePage
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self):
        super().__init__(self.TITLE_LOCATOR, "Все суперцены!")

    TITLE_LOCATOR = (By.XPATH, '//header[@class="b-main-page-blocks-header-2 cfix"]/a')
    CATALOG_TOP_BAR = '//a[contains(@class,"b-main-navigation__link")]/span[text()="{0}"]'
    CATALOG_PAGE_SECTION = '//header[@class="b-main-page-blocks-header-2 cfix"]//a[contains(text(), normalize-space("{0}"))]'
    NEWS_CONTENT = '//div[@class="b-main-page-grid-4 b-main-page-news-2"]'

    def click_on_catalog_top_bar(self, section):
        # catalog_top_bar = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.CATALOG_TOP_BAR, "section", section))
        catalog_top_bar = ELEMENT_FACTORY.get_element(ElementType.BUTTON, (By.XPATH,self.CATALOG_TOP_BAR.format(section)))
        # self.click_on_element(catalog_top_bar)
        catalog_top_bar.click()

    def click_on_catalog_page_section(self, section):
        # catalog_page_section = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.CATALOG_PAGE_SECTION, "section", section))
        catalog_page_section = ELEMENT_FACTORY.get_element(ElementType.BUTTON, (By.XPATH,self.CATALOG_PAGE_SECTION.format(section)))
        # self.click_on_element(catalog_page_section)
        catalog_page_section.click()

    # def verify_main_page(self):
    #     news = self.find_element_by_xpath(self.NEWS_CONTENT)
    #     assert news != None
