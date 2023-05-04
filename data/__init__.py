from json import load

data = load(open('data/config.json', encoding='utf-8'))


def config():
	main_file_name, file_path = data['filename'], data['filepath']
	return main_file_name, file_path


def districts_main_sheet_name():
	return data['districts_main_sheet_name']


def manager_main_sheet_name():
	return data['manager_main_sheet_name']