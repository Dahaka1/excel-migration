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
	columns = [
		"BU",
		"ФИО",
		"Должность",
		"Дата выплаты",
		"Менеджер"
	]
	return columns


def manager_subfile_columns_names() -> list:
	columns = district_subfile_columns_names()
	add_columns = [
		'Бонус из приказа'
	]
	columns.extend(add_columns)
	return columns

