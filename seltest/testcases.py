from django.test.testcases import TestCase
from selenium import selenium

from seltest import config

class SeleniumTestCase(TestCase):

    seleniumHost = config.SELENIUM_HOST
    seleniumPort = config.SELENIUM_PORT
    browserCommand = config.BROWSER_COMMAND
    url = config.DEFAULT_URL

    def selenium_setup(self):
        pass

    def _pre_setup(self):
        super(SeleniumTestCase, self)._pre_setup()
        self.selenium = selenium(
            self.seleniumHost,
            self.seleniumPort,
            self.browserCommand,
            self.url
        )
        self.selenium_setup()
        self.selenium.start()

    def _post_teardown(self):
        super(SeleniumTestCase, self)._post_teardown()
        self.selenium.stop()
