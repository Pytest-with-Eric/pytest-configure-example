
import pytest

def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default")

def pytest_configure(config):
    config.custom_option = config.getoption("--custom-option")
