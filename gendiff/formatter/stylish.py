def get_stylish(first_dict: dict, second_dict: dict) -> str:
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
