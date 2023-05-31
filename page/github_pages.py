from selene import browser, be
from selene.support.shared.jquery_style import s

class GitHubPages:
    def open(self):
        browser.open('')

    def click_desktop_signin(self):
        if browser.element(".header-logged-out").should(be.visible):
            browser.element(".HeaderMenu-link--sign-in").click()
        else:
            print('Element not found')

    def click_mobile_signin(self):
        if browser.element(".header-logged-out").should(be.visible):
            browser.element(".flex-1 > .d-inline-block").click()
        else:
            print('Element not found')
