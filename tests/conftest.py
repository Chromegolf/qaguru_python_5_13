from selene import browser
import pytest

desktop_window  = [(1920, 1080), (1366, 768)]
desktop_ids     = ['desktop (FULL HD)', 'desktop (WXGA)']
mobile_window   = [(412, 915), (390, 844)]
mobile_ids      = ['mobile (Samsung S20 Ultra)', 'mobile (Iphone 12 pro)']

@pytest.fixture(params=desktop_window, ids=desktop_ids)
def desktop_window_size(request):
    return request.param

@pytest.fixture(params=mobile_window, ids=mobile_ids)
def desktop_mobile_size(request):
    return request.param


@pytest.fixture(scope="session", autouse=True)
def set_browser():
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()

