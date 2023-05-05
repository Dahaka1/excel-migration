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

