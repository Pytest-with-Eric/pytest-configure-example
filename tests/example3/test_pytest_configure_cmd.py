
import pytest

def test_custom_option(pytestconfig):
    assert pytestconfig.custom_option == "myValue"  # or any other value passed via command line
