
def get_plain(first_dict: dict, second_dict: dict) -> str:
	p = "Property"
	res_dict = {}
	for key, value in first_dict.items():
		if not second_dict.get(key):
			res_dict[key] = f"{p} '{key}' was removed\n"
	for k, value in second_dict.items():
		value = str(value).lower() if isinstance(value, bool) else value
		if value_2 := first_dict.get(k):
			value_2 = str(
				value_2).lower() if isinstance(value_2, bool) else value_2
			if value != value_2:
				res_dict[
					k] = f"{p} '{k}' was updated. From {value_2} to {value}\n"
		else:
			res_dict[k] = f"{p} '{k}' was added with value: {value}\n"
	res = ""
	for key, value in dict(sorted(res_dict.items())).items():
		res += value
	return res.rstrip()