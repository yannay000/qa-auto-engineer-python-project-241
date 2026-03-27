import argparse


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
    parser.parse_args()
