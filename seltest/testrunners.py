import os
import subprocess
import threading

from django.core.handlers.wsgi import WSGIHandler
from django.core.servers.basehttp import AdminMediaHandler, WSGIServer, WSGIServerException
from django.test.simple import DjangoTestSuiteRunner

from seltest import config
from seltest.handlers import SilentWSGIRequestHandler


class BaseSingleThread(threading.Thread):

    def __init__(self):
        super(BaseSingleThread, self).__init__()
        self.running = threading.Event()
        self.running.set()

    def join(self, timeout=None):
        """Stop the thread and wait for it to finish."""
        self.running.clear()
        threading.Thread.join(self, timeout)

class TestServerThread(BaseSingleThread):
    """Thread for running a http server while tests are running."""

    def run(self):
        try:
            handler = AdminMediaHandler(WSGIHandler())
            server_address = (config.HOST, config.PORT)
            httpd = WSGIServer(server_address, SilentWSGIRequestHandler)
            httpd.set_app(handler)
            while self.running.isSet():
                httpd.handle_request()
            httpd.server_close()
        except WSGIServerException, e:
            pass
        except KeyboardInterrupt:
            os._exit(1)

class SeleniumServerThread(BaseSingleThread):
    """Thread for running a selenium server while tests are running."""

    def run(self):
        self.server_command = "java -jar %s -port %s 2>&1 >> %s" % (
            config.SELENIUM_SERVER_PATH, config.SELENIUM_PORT,
            config.SELENIUM_SERVER_LOGFILE
        )
        subprocess.Popen(self.server_command, shell=True)

    def join(self, timeout=None):
        """Stop the thread and wait for it to finish."""
        super(SeleniumServerThread, self).join(timeout)
        # FIXME: find a clever way to ensure selenium-server is killed
        jar = config.SELENIUM_SERVER_PATH[config.SELENIUM_SERVER_PATH.rfind('/')+1:]
        subprocess.Popen(
            """for pid in $(ps afxu | grep -i "%s" | awk '{print $2}'); do kill "$pid" &> /dev/null; done""" % jar,
            shell=True
        )

class SeleniumBaseTestRunner(DjangoTestSuiteRunner):
    """A basic runner for selenium tests

    Takes care of running django's server and selenium test server
    before starting tests and taking them down after finishing tests.
    """

    def setup_test_environment(self, **kwargs):
        super(SeleniumBaseTestRunner, self).setup_test_environment(**kwargs)
        self.server_thread = TestServerThread()
        self.server_thread.setDaemon(True)
        self.server_thread.start()
        self.selenium_server_thread = SeleniumServerThread()
        self.selenium_server_thread.setDaemon(True)
        self.selenium_server_thread.start()

    def teardown_test_environment(self, **kwargs):
        super(SeleniumBaseTestRunner, self).teardown_test_environment(**kwargs)
        self.server_thread.join(timeout=10)
        self.selenium_server_thread.join(timeout=10)
