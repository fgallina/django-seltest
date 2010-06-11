from django.conf import settings
from django.core.management.commands.test import Command as TestCommand
from django.test import simple

from seltest import config

class Command(TestCommand):

    def handle(self, *test_labels, **options):
        """This overrides normal test runner and test module so
        selenium_tests are run
        """
        settings.TEST_RUNNER = config.TEST_RUNNER
        simple.TEST_MODULE = 'selenium_tests'
        super(Command, self).handle(*test_labels, **options)
