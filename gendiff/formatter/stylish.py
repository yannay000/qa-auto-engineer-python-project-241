def get_stylish(first_dict: dict, second_dict: dict) -> str:
	res = "{\n"
	res_dict = {}
	for key, value in first_dict.items():
		value = str(value).lower() if isinstance(value, bool) else value
		if not second_dict.get(key):
			res_dict[key] = f"  - {key}: {value}\n"
	for key, value in second_dict.items():
		value = str(value).lower() if isinstance(value, bool) else value
		if value_2 := first_dict.get(key):
			value_2 = str(
				value_2).lower() if isinstance(value_2, bool) else value_2
			if value == value_2:
				res_dict[key] = f"    {key}: {value}\n"
			else:
				res_dict[key] = f"  - {key}: {value_2}\n  + {key}: {value}\n"
		else:
			res_dict[key] = f"  + {key}: {value}\n"
	for key, value in dict(sorted(res_dict.items())).items():
		res += value
	res += "}"
	return res
