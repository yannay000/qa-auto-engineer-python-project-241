from gendiff import generate_diff
from tests.test_data.result_string import (
    json_string,
    plain_string,
    stylish_string,
)


def test_yml_stylish():

    diff = generate_diff("files/file1.yml", "files/file2.yml")
    assert diff == stylish_string, (
            f"Incorrect result {diff} != expected result {stylish_string}"
    )


def test_yml_plain():

    diff = generate_diff("files/file1.yml", "files/file2.yml", format="plain")
    assert diff == plain_string, (
        f"Incorrect result {diff} != expected result {plain_string}"
    )


def test_yml_json():

    diff = generate_diff("files/file1.yml", "files/file2.yml", format="json")
    assert diff == json_string, (
        f"Incorrect result {diff} != expected result {json_string}"
    )