import pytest
from selene import browser, be
from page.github_pages import GitHubPages
from tests.conftest import desktop_window, desktop_ids, mobile_window, mobile_ids, set_browser


@pytest.fixture(params=desktop_window + mobile_window, ids=desktop_ids + mobile_ids)
def init_browser(request):
    browser.config.window_width = request.param[0] ## ширина
    browser.config.window_height = request.param[1] ## высота
    yield request.node.callspec.id
    browser.quit()


@pytest.mark.parametrize('init_browser', desktop_window, indirect=True)
def test_github_desktop(init_browser):
    page = GitHubPages()
    page.open()
    page.click_desktop_signin()

@pytest.mark.parametrize('init_browser', mobile_window, indirect=True)
def test_github_mobile(init_browser):
    page = GitHubPages()
    page.open()
    page.click_mobile_signin()
