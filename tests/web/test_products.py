import pytest
from pages.products_page import ProductsPage

@pytest.mark.web
def test_product_list_visible(page, config):
    products = ProductsPage(page)
    products.navigate(config.get_base_url() + "/products")
    assert products.is_product_list_visible()


@pytest.mark.web
def test_search_functionality(page, config):
    products = ProductsPage(page)
    products.navigate(config.get_base_url() + "/products")
    products.search("Tshirt")
    assert products.is_search_result_displayed()

