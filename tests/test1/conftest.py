import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "basic: mark test as basic operation test")