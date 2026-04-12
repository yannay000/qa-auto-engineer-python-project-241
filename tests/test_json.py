from gendiff import generate_diff
from tests.test_data.result_string import (
    json_string,
    plain_string,
    stylish_string,
)


def test_json_stylish():

    diff = generate_diff("files/file1.json", "files/file2.json")
    assert diff == stylish_string, (
        f"Incorrect result {diff} != expected result {stylish_string}"
    )


def test_json_plain():

    diff = generate_diff("files/file1.json", "files/file2.json", format="plain")
    assert diff == plain_string, (
            f"Incorrect result {diff} != expected result {plain_string}"
    )


def test_json_json():

    diff = generate_diff("files/file1.json", "files/file2.json", format="json")
    assert diff == json_string, (
            f"Incorrect result {diff} != expected result {json_string}"
    )