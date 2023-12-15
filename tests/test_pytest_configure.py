
def test_display_input(input_file_content):
    print("Content from input file:")
    print(input_file_content)
    assert "Pytest with Eric" in input_file_content
