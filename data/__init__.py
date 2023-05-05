from json import load

data = load(open('data/config.json', encoding='utf-8'))


def config():
	main_file_name, file_path = data['filename'], data['filepath']
	return main_file_name, file_path


def districts_main_sheet_name():
	return data['districts_main_sheet_name']


def manager_main_sheet_name():
	return data['manager_main_sheet_name']


def folder_names():
	return data['managers_folder_name'], data['districts_folder_name']


def managers_additional_columns():
	return data['additional_managers_columns']


def general_file_sheets_names():
	return data['general_file_sheets_names']


def subfile_file_base_columns_titles():
	return data['subfile_base_columns_titles']