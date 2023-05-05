from typing import Optional

import data
import secondary_funcs
from classes.employee import Worker


def find_workers() -> Optional[list]:
	"""
	:return: list of all units available in main Excel table
	"""
	sheets_names = data.general_file_sheets_names()
	if secondary_funcs.files_checking():
		workers_worksheet = secondary_funcs.read_main_file(sheet_name=sheets_names[0])
		positions_worksheet = secondary_funcs.read_main_file(sheet_name=sheets_names[1])
		current_column = "B"
		counter = 2
		workers_list = []
		while True:
			worker = workers_worksheet[f"{current_column}{counter}"].value
			if not worker is None:
				worker = Worker(
					fullname=worker,
					workers_worksheet=workers_worksheet,
					positions_worksheet=positions_worksheet
				)
				workers_list.append(worker)
				counter += 1
			else:
				return workers_list
	return None
