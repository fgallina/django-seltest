from seltest.testcases import SeleniumTestCase
from seltest import config

class TestGoogle(SeleniumTestCase):

    def testSearch(self):
        sel = self.selenium
        sel.open("http://www.google.com")
        sel.type("q", "seltest")
        sel.click("btnG")
        sel.wait_for_page_to_load(5000)
        self.failUnless("Google" in sel.get_title())
