def get_json(first_dict: dict, second_dict: dict) -> str:
	merged_dict = first_dict | second_dict
	res = "{\n"
	for key, value in merged_dict.items():
		if isinstance(value, bool):
			value = str(value).lower()
		elif isinstance(value, str):
			value = f'"{value}"'
		res += f'  "{key}": {value},\n'
	res = res.rstrip(",\n")
	res += "\n}"
	return res
