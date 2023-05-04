import data
import secondary_funcs
from classes.employee import *

workers = secondary_funcs.find_all_workers()
main_folder = data.config()[1]
workers_params = secondary_funcs.unpack_workers(workers)


def create_general_workbook():
	excel_file_params = secondary_funcs.sheet_params(excel_file_type='districts')
	folder_name = "districts"
	# sorting by districts
	districts_dict = dict()
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
			worksheet = workbook["Общий"]
			for worker in district_workers:
				worksheet.append(worker)
			workbook = secondary_funcs.format_columns(workbook, sheet_name="Общий")  # auto-adjusting
			workbook.save(filepath)
			workbook.close()


def create_managers_workbooks():
	excel_file_params = secondary_funcs.sheet_params(excel_file_type='managers')
	folder_name = "managers"
	# sorting by managers
	managers_dict = dict()
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
			worksheet = workbook["Менеджер"]
			for worker in manager_workers:
				worksheet.append(worker)
			workbook = secondary_funcs.format_columns(workbook, sheet_name="Менеджер")  # auto-adjusting
			workbook.save(filepath)
			workbook.close()


def updating() -> NoReturn:
	secondary_funcs.secondary_directories_init(main_folder)
	create_general_workbook()
	create_managers_workbooks()


def update_files() -> NoReturn:
	updating()

