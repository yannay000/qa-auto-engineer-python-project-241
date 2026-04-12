from gendiff.scripts.gendiff import pars_args
from tests.test_data.path import path_1, path_2


def test_pars_args():
	args = pars_args(args=[path_1, path_2])
	assert args.first_file == (
		path_1), f"Incorrect first_file argument: {args.first_file}"
	assert args.second_file == (
		path_2), f"Incorrect second_file argument: {args.second_file}"
	assert args.extension == (
		"json"), f"Incorrect extension argument: {args.extension}"
	assert args.format == (
		"stylish"), f"Incorrect format argument: {args.format}"
