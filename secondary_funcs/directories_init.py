import os
import os.path
from typing import NoReturn

import data


def init() -> NoReturn:
	folder = data.config()[1]
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
