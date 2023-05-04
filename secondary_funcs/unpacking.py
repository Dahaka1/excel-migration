def unpack(units_list) -> tuple:
	if not units_list is None:
		unpacked_workers = [
			(worker.district,
			worker.fullname,
			worker.working_position.name,
			worker.updating_date,
			worker.manager_name) for worker in units_list
		]
		return tuple(unpacked_workers)
