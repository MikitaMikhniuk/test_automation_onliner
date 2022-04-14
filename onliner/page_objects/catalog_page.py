from selenium.webdriver.common.by import By
from framework.base_page import BasePage
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType



class CatalogPage(BasePage):

    def __init__(self):
        super().__init__(self.HEADER, "КаталогВсе суперцены!")

    HEADER = (By.XPATH, "//div[@class='catalog-navigation__title']")
    NAV_CLASS = '//span[contains(@class,"catalog-navigation-classifier__item-title-wrapper") and translate(text(),"\u00A0"," ")="{0}"]'
    ASIDE_LIST = (
        By.XPATH, '//div[@class="catalog-navigation-list__aside-list"]')
    NAV_SUBCLASS = '//div[contains(@class,"catalog-navigation-list__aside-title") and translate(normalize-space(text()),"\u00A0"," ")="{0}"]'
    NAV_LIST = (By.XPATH, '//div[@class="catalog-navigation-list__dropdown"]')
    ASIDE_ITEM = '//span[contains(@class,"catalog-navigation-list__dropdown-title") and translate(normalize-space(text()),"\u00A0"," ")="{0}"]'
    LOADING_BAR = (
        By.XPATH, '//div[@class="schema-products schema-products_processing"]')
    CATALOG_HEADER_FULL = '//div[@class="catalog-navigation__title"]'
    CATALOG_HEADER_SUPERPRICE = '//div[@class="catalog-navigation__title"]//a'

    def navigate_to_menu(self, section):
        # nav_class = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.NAV_CLASS, "section", section))
        nav_class = ELEMENT_FACTORY.get_element(ElementType.BUTTON, (By.XPATH, self.NAV_CLASS.format(section)))
        # self.click_on_element(nav_class)
        nav_class.click()
        # wait_until = Until(self.driver)
        # wait_until.visibility_of_any_elements_located(self.ASIDE_LIST)

    def navigate_to_submenu(self, section):
        # nav_subclass = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.NAV_SUBCLASS, "section", section))
        nav_subclass = ELEMENT_FACTORY.get_element(ElementType.BUTTON, (By.XPATH, self.NAV_SUBCLASS.format(section)))
        # self.click_on_element(nav_subclass)
        nav_subclass.click()
        # wait_until = Until(self.driver)
        # wait_until.visibility_of_any_elements_located(self.NAV_LIST)

    def click_on_submenu_item(self, section):
        # aside_item = self.find_element_by_xpath(self.get_locator_with_replaced_xpath(self.ASIDE_ITEM, "section", section))
        aside_item = ELEMENT_FACTORY.get_element(ElementType.BUTTON, (By.XPATH, self.ASIDE_ITEM.format(section)))
        # self.click_on_element(aside_item)
        aside_item.click()

    # def verify_catalog_page_by_header(self, header):
    #     catalog_header_whole = self.find_element_by_xpath(
    #         self.CATALOG_HEADER_FULL)
    #     catalog_super_price = self.find_element_by_xpath(
    #         self.CATALOG_HEADER_SUPERPRICE)
    #     catalog_header = catalog_header_whole.text.replace(
    #         catalog_super_price.text, '')
    #     assert catalog_header == header
    #     return catalog_header
