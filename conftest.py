from __future__ import annotations

import pytest
import requests
from playwright.sync_api import sync_playwright

from apis.brands_api import BrandsApi
from apis.categories_api import CategoriesApi
from apis.products_api import ProductsApi
from apis.search_api import SearchApi
from apis.users_api import UsersApi
from utils.config_reader import ConfigReader


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--headed", action="store_true", default=False)
    parser.addoption("--resolution", action="store", default="0")


@pytest.fixture(scope="session")
def config() -> ConfigReader:
    return ConfigReader()


@pytest.fixture(scope="session")
def base_url(config: ConfigReader) -> str:
    return config.get_base_url()


@pytest.fixture(scope="session")
def api_url(config: ConfigReader) -> str:
    return config.get_api_url()


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope="session")
def browser(request: pytest.FixtureRequest, config: ConfigReader):
    with sync_playwright() as p:
        browser_name = request.config.getoption("--browser")
        headed = bool(request.config.getoption("--headed"))
        headless = not headed

        if browser_name == "chromium":
            b = p.chromium.launch(headless=headless)
        elif browser_name == "firefox":
            b = p.firefox.launch(headless=headless)
        elif browser_name == "webkit":
            b = p.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        yield b
        b.close()


@pytest.fixture(scope="function")
def browser_context(browser, request: pytest.FixtureRequest, config: ConfigReader):
    resolutions = config.get_resolutions()
    idx = int(request.config.getoption("--resolution"))
    viewport = None
    if resolutions and 0 <= idx < len(resolutions):
        width, height = resolutions[idx]
        viewport = {"width": width, "height": height}

    ctx = browser.new_context(viewport=viewport)
    yield ctx
    ctx.close()


@pytest.fixture(scope="function")
def page(browser_context):
    p = browser_context.new_page()
    p.on("dialog", lambda d: d.accept())
    yield p
    p.close()


@pytest.fixture(scope="session")
def products_api(api_url: str, api_client) -> ProductsApi:
    return ProductsApi(api_url, api_client)


@pytest.fixture(scope="session")
def brands_api(api_url: str, api_client) -> BrandsApi:
    return BrandsApi(api_url, api_client)


@pytest.fixture(scope="session")
def categories_api(api_url: str, api_client) -> CategoriesApi:
    return CategoriesApi(api_url, api_client)


@pytest.fixture(scope="session")
def search_api(api_url: str, api_client) -> SearchApi:
    return SearchApi(api_url, api_client)


@pytest.fixture(scope="session")
def users_api(api_url: str, api_client) -> UsersApi:
    return UsersApi(api_url, api_client)