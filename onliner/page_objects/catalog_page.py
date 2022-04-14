from selenium.webdriver.common.by import By
from framework.base_page import BasePage
from framework.elements.element_factory import ELEMENT_FACTORY, ElementType


class CatalogPage(BasePage):

    def __init__(self):
        super().__init__(self.HEADER, "КаталогВсе суперцены!")

    HEADER = (By.XPATH, "//div[@class='catalog-navigation__title']")
    NAV_CLASS = '//span[contains(@class,"catalog-navigation-classifier__item-title-wrapper") and translate(text(),"\u00A0"," ")="{0}"]'
    NAV_SUBCLASS = '//div[contains(@class,"catalog-navigation-list__aside-title") and translate(normalize-space(text()),"\u00A0"," ")="{0}"]'
    ASIDE_ITEM = '//span[contains(@class,"catalog-navigation-list__dropdown-title") and translate(normalize-space(text()),"\u00A0"," ")="{0}"]'

    def navigate_to_menu(self, section):
        nav_class = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, (By.XPATH, self.NAV_CLASS.format(section)))
        nav_class.click()

    def navigate_to_submenu(self, section):
        nav_subclass = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, (By.XPATH, self.NAV_SUBCLASS.format(section)))
        nav_subclass.click()

    def click_on_submenu_item(self, section):
        aside_item = ELEMENT_FACTORY.get_element(
            ElementType.BUTTON, (By.XPATH, self.ASIDE_ITEM.format(section)))
        aside_item.click_and_wait()
