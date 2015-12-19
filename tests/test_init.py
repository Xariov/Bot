import pytest


class BotTests(object):

    def test_initialization(self):
        """ Make sure test suite is running properly """
        assert 2 + 2 == 4

    def test_import(self):
        import bot
