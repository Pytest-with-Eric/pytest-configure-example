import pytest
import os

def pytest_configure(config):
    # Get the path to the text file in the same directory as conftest.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_directory, "input.txt")

    # Read the content of the file and store it in the pytest config object
    with open(input_file_path, "r") as file:
        file_content = file.read()
    config._input_file_content = file_content  # Store the file content in the pytest config object

@pytest.fixture
def input_file_content(request):
    return request.config._input_file_content
