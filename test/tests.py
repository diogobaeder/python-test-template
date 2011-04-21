import core # just a placeholder to put production code

from nose.tools import raises

# method tests
class TestExample(object):

    def test_should_have_success(self):
        assert core.willSucceed()

    @raises(AssertionError)
    def test_should_fail(self):
        assert core.willFail()

    @raises(Exception)
    def test_should_raise_exception(self):
        assert core.willRaiseException()

# function tests
def test_should_have_success():
    assert core.willSucceed()
