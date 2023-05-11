import data


def months() -> dict:
	months_list = [
		'январь',
		'февраль',
		'март',
		'апрель',
		'май',
		'июнь',
		'июль',
		'август',
		'сентябрь',
		'октябрь',
		'ноябрь',
		'декабрь']
	return {months_list.index(i) + 1: i.title() for i in months_list}


def district_subfile_columns_names() -> list:
	columns = data.subfile_file_base_columns_titles()
	return columns


def manager_subfile_columns_names() -> list:
	columns = district_subfile_columns_names()
	add_columns = data.managers_additional_columns()
	columns.extend(add_columns)
	return columns


def bonus_formula(column: str, row: int, worker: tuple) -> str:
	district, manager_name = worker[0], worker[4]
	# main_file_row = worker[5]
	# main_file_cell = f'B{main_file_row}'
	manager_sheet_name = data.manager_main_sheet_name()
	bonus_cell = f'${column}${row}'
	sub_files_folder = data.sub_main_folder_name()
	file_name = f'{district}_{manager_name}.xlsx'
	formula = f"='[\\{sub_files_folder}\\{district}\\{file_name}]{manager_sheet_name}'!{bonus_cell}"
	return formula
