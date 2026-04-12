import json

import yaml

from gendiff.formatter.json_format import get_json
from gendiff.formatter.plain import get_plain
from gendiff.formatter.stylish import get_stylish


def read_json(file_name: str):
	try:
		result = json.load(open(file_name))
	except FileNotFoundError:
		return f"Couldn't find file with this path: {file_name}"
	return result


def read_yml(file_name: str):
	try:
		with open(file_name, 'r') as file:
			result = yaml.safe_load(file)
	except FileNotFoundError:
		return f"Couldn't find file with this path: {file_name}"
	return result


def generate_result(first_dict: dict, second_dict: dict, format: str) -> str:
	if not format or format == "stylish":
		return get_stylish(first_dict, second_dict)
	elif format == "plain":
		return get_plain(first_dict, second_dict)
	elif format == "json":
		return get_json(first_dict, second_dict)
	else:
		return f"Unknown output format: {format}"


def generate_diff(file_path1: str, file_path2: str, format: str | None = None):
	file_format = file_path1.split(".")[1]
	if file_format == "json":
		first_dict = read_json(file_path1)
		second_dict = read_json(file_path2)
	elif file_format == "yml":
		first_dict = read_yml(file_path1)
		second_dict = read_yml(file_path2)
	else:
		return ""
	if isinstance(first_dict, str) or isinstance(second_dict, str):
		print(f"{first_dict}\n{second_dict}")
		return
	result = generate_result(first_dict, second_dict, format)
	return result
