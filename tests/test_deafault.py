from gendiff import generate_diff
from tests.test_data.result_string import default_string

def test_default():

    diff = generate_diff("file1.json", "file2.json")
    assert diff == default_string, f"Incorrect result {diff} != expected result {default_string}"