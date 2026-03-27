import argparse
import json


def read_json(file_name: str):
	path = f"files/{file_name}"
	try:
		result = json.load(open(path))
	except FileNotFoundError:
		return f"Couldn't find file with this path {path}"
	return result
    

def main():
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
    if args.format == "json":
        print(read_json(args.first_file))
        print(read_json(args.second_file))
