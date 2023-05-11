import secondary_funcs
from data.additional_info import *

sub_main_folder_name = data.sub_main_folder_name()
excel_params = data.excel_params()


def general_params():
	workers = secondary_funcs.find_all_workers()
	workers_params = secondary_funcs.unpack_workers(workers)
	main_folder = data.config()[1]
	return workers_params, main_folder


def create_general_workbook():
	excel_file_params = secondary_funcs.sheet_params(excel_file_type=excel_params[0])
	main_sheet_name = data.districts_main_sheet_name()
	# sorting by districts
	districts_dict = dict()
	workers_params, main_folder = general_params()
	for unit in workers_params:
		try:
			districts_dict[unit[0].rstrip()].append(unit)
		except KeyError:
			districts_dict[unit[0].rstrip()] = [unit]
	for district in districts_dict:
		if not district is None:
			district_name = district.rstrip()
			district_workers = sorted(districts_dict[district], key=lambda params: params[0])
			folder_path = secondary_funcs.sub_folder_init(district_name)
			filepath = f"{folder_path}/{district_name}.xlsx"
			workbook = secondary_funcs.create_excel(excel_file_params)
			worksheet = workbook[main_sheet_name]
			for worker in district_workers:
				worksheet.append(worker)
			workbook = secondary_funcs.format_columns(workbook, sheet_name=main_sheet_name)  # auto-adjusting
			workbook.save(filepath)
			workbook.close()


def create_managers_workbooks():
	main_file_workbook, main_file_name, main_file_main_sheet_name = secondary_funcs.main_workbook(), data.config()[0], data.main_sheet_name()
	main_worksheet = main_file_workbook[main_file_main_sheet_name]
	excel_file_params = secondary_funcs.sheet_params(excel_file_type=excel_params[1])
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
			filepath = f"{main_folder}/{sub_main_folder_name}/{business_unit}/{business_unit}_{manager_name}.xlsx"
			# folder_names[1] because reformat directories structure was needed
			workbook = secondary_funcs.create_excel(excel_file_params)
			worksheet = workbook[main_sheet_name]
			for worker in manager_workers:
				worksheet.append(worker[:-1])
				# adding some formulas
				# cannot add it using additional packages funcs - updating main workbook problem
				main_file_worker_row = worker[-1]
				row = manager_workers.index(worker) + 2
				bonus_column = data.bonus_column()
				main_worksheet[f"{bonus_column}{main_file_worker_row}"].value = bonus_formula(bonus_column, row, worker)
			workbook = secondary_funcs.auto_format_columns(workbook, sheet_name=main_sheet_name)  # auto-adjusting
			workbook.save(filepath)
	main_file_workbook.save(f"{main_folder}/{main_file_name}")


def updating() -> None:
	main_folder = general_params()[1]
	secondary_funcs.secondary_directories_init(main_folder)
	create_general_workbook()
	create_managers_workbooks()


def update_files() -> None:
	updating()
