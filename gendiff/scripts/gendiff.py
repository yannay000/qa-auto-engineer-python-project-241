import argparse

from gendiff.scripts.parser import generate_diff


def pars_args(args=None):
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="first file name")
    parser.add_argument("second_file", type=str, help="second file name")
    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        default="json",
        help="set format of the input file"
	)
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="stylish",
        help="set format of output"
    )
    args = parser.parse_args(args)
    print(args.first_file)
    print(args.extension)
    if args.first_file.endswith(
        args.extension) and args.second_file.endswith(args.extension):
        return args
    else:
        return


def main():
    args = pars_args()
    if args:
        result = generate_diff(
            args.first_file, args.second_file, format=args.format
        )
        print(result)
    else:
        print("Incorrect file extension")
