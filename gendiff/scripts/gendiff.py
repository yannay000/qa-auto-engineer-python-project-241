import argparse
import json


def read_json(file_name: str):
	path = f"files/{file_name}"
	try:
		result = json.load(open(path))
	except FileNotFoundError:
		return f"Couldn't find file with this path {path}"
	return result

def pars_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="first file name")
    parser.add_argument("second_file", type=str, help="second file name")
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="json",
        help="set format of output"
	)
    args = parser.parse_args()
    return args

def generate_diff(file_path1: str, file_path2: str):
    first_dict = read_json(file_path1)
    second_dict = read_json(file_path2)
    res = "{\n"
    for key, value in first_dict.items():
        if not second_dict.get(key):
            res += f"  - {key}: {value}\n"
    for key, value in second_dict.items():
        if value_2:= first_dict.get(key):
            if value == value_2:
                res += f"    {key}: {value}\n"
            else:
                res += f"  - {key}: {value_2}\n"
                res += f"  + {key}: {value}\n"
        else:
            res += f"  + {key}: {value}\n"
    # for key, value in second_dict.items():
    #     if not first_dict.get(key):
    #         res += f"  + {key}: {value}\n"
    res += "}"
    # print(res)
    return res


def main():
    args = pars_args()
    if args.format == "json":
        generate_diff(args.first_file, args.second_file)
    # if args.format == "json":
    #     first_dict = read_json(args.first_file)
    #     second_dict = read_json(args.second_file)
