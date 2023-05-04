import os
import os.path
from typing import NoReturn

import data


def init() -> NoReturn:
	filename, folder = data.config()
	if os.path.exists(filename):
		if not os.path.exists(folder):
			os.mkdir(folder)
		if not os.path.exists(f'{folder}/districts'):
			os.mkdir(f'{folder}/districts')
		if not os.path.exists(f'{folder}/managers'):
			os.mkdir(f'{folder}/managers')


def init_secondary(path) -> NoReturn:
	paths = ["managers", "districts"]
	for p in paths:
		if not os.path.exists(f"{path}/{p}"):
			os.mkdir(f'{path}/{p}')
