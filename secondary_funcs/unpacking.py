def unpack(units_list) -> tuple:
	unpacked_workers = [
		(worker.district,
		worker.fullname,
		worker.working_position.name,
		worker.updating_date,
		worker.manager_name) for worker in units_list
	]
	return tuple(unpacked_workers)
