import pytest
from selene import browser, be
from page.github_pages import GitHubPages
from tests.conftest import desktop_window, desktop_ids, mobile_window, mobile_ids


def test_github_desktop(desktop_window_size):
    page = GitHubPages()

    browser.config.window_width = desktop_window_size[0] ## ширина
    browser.config.window_height = desktop_window_size[1] ## высота

    page.open()
    page.click_desktop_signin()

def test_github_mobile(desktop_mobile_size):
    page = GitHubPages()

    browser.config.window_width = desktop_mobile_size[0]  ## ширина
    browser.config.window_height = desktop_mobile_size[1]  ## высота

    page.open()
    page.click_mobile_signin()
