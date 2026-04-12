from gendiff import generate_diff
from tests.test_data.result_string import stylish_string, plain_string

def test_json_stylish():

    diff = generate_diff("file1.json", "file2.json")
    assert diff == stylish_string, f"Incorrect result {diff} != expected result {stylish_string}"

def test_json_plain():

    diff = generate_diff("file1.json", "file2.json", format="plain")
    assert diff == plain_string, f"Incorrect result {diff} != expected result {plain_string}"