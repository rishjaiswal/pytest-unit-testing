import pytest
print("Start Execution of Program")

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    print("Start richa SetupModule of Program")

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print("Start richa TearDownModule of Program")

@pytest.fixture
def anshu():
    print("Called Fixture")

def test_richa(anshu):
    print("Start test_richa_method")
    assert True



