from django.conf import settings

TEST_RUNNER = getattr(settings, 'SELTEST_TEST_RUNNER', 'seltest.testrunners.SeleniumBaseTestRunner')

HOST = getattr(settings, 'SELTEST_HOST', '127.0.0.1')
PORT = getattr(settings, 'SELTEST_PORT', 8001)

SELENIUM_HOST = getattr(settings, 'SELTEST_SELENIUM_HOST', '127.0.0.1')
SELENIUM_PORT = getattr(settings, 'SELTEST_SELENIUM_PORT', 4444)
BROWSER_COMMAND = getattr(settings, 'SELTEST_BROWSER_COMMAND', "*firefox")
DEFAULT_URL = getattr(
    settings, 'SELTEST_DEFAULT_URL',
    "http://%s:%s" % (HOST, PORT)
)

SELENIUM_SERVER_PATH = getattr(settings, 'SELTEST_SELENIUM_SERVER_PATH', '/opt/selenium-server.jar')
SELENIUM_SERVER_ARGS = getattr(settings, 'SELTEST_SELENIUM_SERVER_ARGS', "-port %s" % SELENIUM_PORT)

SERVER_LOGFILE = getattr(settings, 'SELTEST_SERVER_LOGFILE', "/tmp/seltest_testserver.log")
SELENIUM_SERVER_LOGFILE = getattr(settings, 'SELTEST_SELENIUM_SERVER_LOGFILE', "/tmp/seltest_seleniumserver.log")
