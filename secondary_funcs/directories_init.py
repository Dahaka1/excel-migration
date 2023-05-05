import os
import os.path

import data

sub_folders_names = data.sub_main_folder_name()


def init() -> None:
	filename, folder = data.config()
	if os.path.exists(filename):
		if not os.path.exists(folder):
			os.mkdir(folder)
		if not os.path.exists(f'{folder}/{sub_folders_names[1]}'):
			os.mkdir(f'{folder}/{sub_folders_names[1]}')
		# if not os.path.exists(f'{folder}/{sub_folders_names[0]}'):
		# 	os.mkdir(f'{folder}/{sub_folders_names[0]}')
		# (changed by request from client)


def init_secondary(path) -> None:
	folder = sub_folders_names
	full_path = f'{path}/{folder}'
	if not os.path.exists(full_path):
		os.mkdir(full_path)


def init_district_folder(district) -> str:
	main_folder = data.config()[1]
	sub_folder = sub_folders_names
	path = f"{main_folder}/{sub_folder}/{district}"
	if not os.path.exists(path):
		os.mkdir(path)
	return path
