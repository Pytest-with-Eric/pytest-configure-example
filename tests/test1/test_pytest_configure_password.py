import pytest

@pytest.mark.password
def test_password_format(pytestconfig):
    password = input("Enter a password for testing: ")
    assert pytestconfig.password_pattern.match(password), "Password does not meet the required format"
