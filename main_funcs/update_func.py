import data
import secondary_funcs


folder_names = data.folder_names()


def general_params():
	workers = secondary_funcs.find_all_workers()
	workers_params = secondary_funcs.unpack_workers(workers)
	main_folder = data.config()[1]
	return workers_params, main_folder


def create_general_workbook():
	folder_name = folder_names[1]
	excel_file_params = secondary_funcs.sheet_params(excel_file_type=folder_name)
	main_sheet_name = data.districts_main_sheet_name()
	# sorting by districts
	districts_dict = dict()
	workers_params, main_folder = general_params()
	for unit in workers_params:
		try:
			districts_dict[unit[0]].append(unit)
		except KeyError:
			districts_dict[unit[0]] = [unit]
	for district in districts_dict:
		if not district is None:
			district_name = district.rstrip()
			district_workers = sorted(districts_dict[district], key=lambda params: params[0])
			filepath = f"{main_folder}/{folder_name}/{district_name}.xlsx"
			workbook = secondary_funcs.create_excel(excel_file_params)
			worksheet = workbook[main_sheet_name]
			for worker in district_workers:
				worksheet.append(worker)
			workbook = secondary_funcs.format_columns(workbook, sheet_name=main_sheet_name)  # auto-adjusting
			workbook.save(filepath)
			workbook.close()


def create_managers_workbooks():
	folder_name = folder_names[0]
	excel_file_params = secondary_funcs.sheet_params(excel_file_type=folder_name)
	main_sheet_name = data.manager_main_sheet_name()
	# sorting by managers
	managers_dict = dict()
	workers_params, main_folder = general_params()
	for unit in workers_params:
		try:
			managers_dict[unit[4]].append(unit)
		except KeyError:
			managers_dict[unit[4]] = [unit]
	for manager in managers_dict:
		if not manager is None:
			manager_name = manager.rstrip()
			manager_workers = sorted(managers_dict[manager], key=lambda params: params[1])
			business_unit = managers_dict[manager][0][0]
			filepath = f"{main_folder}/{folder_name}/{business_unit} - {manager_name}.xlsx"
			workbook = secondary_funcs.create_excel(excel_file_params)
			worksheet = workbook[main_sheet_name]
			for worker in manager_workers:
				worksheet.append(worker)
			workbook = secondary_funcs.format_columns(workbook, sheet_name=main_sheet_name)  # auto-adjusting
			workbook.save(filepath)
			workbook.close()


def updating() -> None:
	main_folder = general_params()[1]
	secondary_funcs.secondary_directories_init(main_folder)
	create_general_workbook()
	create_managers_workbooks()


def update_files() -> None:
	updating()

