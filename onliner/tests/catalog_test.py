from framework.utils import json_reader
from onliner.page_objects.main_page import MainPage
from onliner.page_objects.catalog_page import CatalogPage
from onliner.page_objects.result_page import ResultPage

test_data_path = "onliner\\resources\\test_data.json"
test_data = json_reader.get_json(test_data_path)

def test_onliner_tv_flow(setup):
 
    main_page = MainPage()
    main_page.onliner_header.click_on_catalog_top_bar("Каталог")

    catalog = CatalogPage()
    catalog.navigate_to_menu("Электроника")
    catalog.navigate_to_submenu("Телевидение и видео")
    catalog.click_on_submenu_item("Телевизоры")

    results = ResultPage()
    results.click_on_filter_checkbox(test_data["VENDOR"])
    results.set_max_price(test_data["MAX_PRICE"])
    results.click_on_filter_checkbox(test_data["RESOLUTION"])
    results.set_min_size(test_data["MIN_SIZE"])
    results.set_max_size(test_data["MAX_SIZE"])
    
    results.assert_headers(test_data["VENDOR"])
    results.assert_descriptions(
        test_data["RESOLUTION"], test_data["MIN_SIZE"], test_data["MAX_SIZE"])
    results.assert_prices(test_data["MAX_PRICE"])
