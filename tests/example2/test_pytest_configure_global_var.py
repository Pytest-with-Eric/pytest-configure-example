
import pytest

def test_example(request):
    # Retrieve the global variable from the pytest configuration
    global_value = request.config.my_global_variable

    print(f"The global variable is: {global_value}")
