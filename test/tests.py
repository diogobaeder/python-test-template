from core import *

class TestExample(object):

    def test_should_have_success(self):
        assert willSucceed()

    def test_should_fail(self):
        assert willFail(), "Failures will be notified. Comment this assertion to see all green again."
        assert willRaiseException()
        assert willSucceed()
