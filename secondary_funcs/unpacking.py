from typing import Optional


def unpack(units_list) -> Optional[tuple]:
	"""
	:return: unpacked list of all units in needed format for using when adding to resulting Excel files
	"""
	if not units_list is None:
		unpacked_workers = [
			(worker.district,
			 worker.fullname,
			 worker.working_position.name,
			 worker.updating_date,
			 worker.manager_name,
			 worker.excel_file_row_number) for worker in units_list
		]
		return tuple(unpacked_workers)
	return None
