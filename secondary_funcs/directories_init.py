import os
import os.path

import data

sub_folders_names = data.folder_names()


def init() -> None:
	filename, folder = data.config()
	if os.path.exists(filename):
		if not os.path.exists(folder):
			os.mkdir(folder)
		if not os.path.exists(f'{folder}/{sub_folders_names[1]}'):
			os.mkdir(f'{folder}/{sub_folders_names[1]}')
		if not os.path.exists(f'{folder}/{sub_folders_names[0]}'):
			os.mkdir(f'{folder}/{sub_folders_names[0]}')


def init_secondary(path) -> None:
	paths = sub_folders_names
	for p in paths:
		if not os.path.exists(f"{path}/{p}"):
			os.mkdir(f'{path}/{p}')
