import json

import yaml


def read_json(file_name: str):
	path = f"files/{file_name}"
	try:
		result = json.load(open(path))
	except FileNotFoundError:
		return f"Couldn't find file with this path {path}"
	return result


def read_yml(file_name: str):
	path = f"files/{file_name}"
	try:
		with open(path, 'r') as file:
			result = yaml.safe_load(file)
	except FileNotFoundError:
		return f"Couldn't find file with this path {path}"
	return result


def generate_result(first_dict: dict, second_dict: dict, style: str) -> str:
	if not style or style == "stylish":
		res = "{\n"
		for key, value in first_dict.items():
			if not second_dict.get(key):
				res += f"  - {key}: {value}\n"
		for key, value in second_dict.items():
			if value_2 := first_dict.get(key):
				if value == value_2:
					res += f"    {key}: {value}\n"
				else:
					res += f"  - {key}: {value_2}\n"
					res += f"  + {key}: {value}\n"
			else:
				res += f"  + {key}: {value}\n"
		res += "}"
		return res
	else:
		return f"Unknown output style: {style}"


def generate_diff(file_path1: str, file_path2: str, style: str | None = None):
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
	result = generate_result(first_dict, second_dict, style)
	return result
