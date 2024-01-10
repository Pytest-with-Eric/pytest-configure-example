import re
import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "password: mark a test to check password formatting"
    )

    config.password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&-])[A-Za-z\d@$!%*?&-]{8,}$')


