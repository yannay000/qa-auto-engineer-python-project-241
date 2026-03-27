import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="First file name")
    parser.add_argument("second_file", type=str, help="Second file name")
    parser.parse_args()
    return