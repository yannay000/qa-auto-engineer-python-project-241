from gendiff.scripts.gendiff import pars_args

def test_pars_args():
	args = pars_args(args=['files/test1.json', 'files/test2.json'])
	assert args.first_file == 'files/test1.json', f"Incorrect first_file argument: {args.first_file}"
	assert args.second_file == 'files/test2.json', f"Incorrect second_file argument: {args.second_file}"
	assert args.extension == "json", f"Incorrect extension argument: {args.extension}"
	assert args.format == "stylish", f"Incorrect format argument: {args.format}"
