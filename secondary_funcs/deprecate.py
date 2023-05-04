import os
import data

main_file_name, file_folder = data.config()


def main_file_checking():
	return os.path.exists(f'{file_folder}/{main_file_name}')