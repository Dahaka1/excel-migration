from openpyxl import Workbook
from openpyxl.styles import Font

from data.additional_info import *


def create_excel_table(sheets_info: dict) -> Workbook:
	"""
	:param sheets_info: dict with sheet names as keys and title columns as values
	"""
	workbook = Workbook()
	for sheet in sheets_info:
		title_columns = sheets_info[sheet]
		workbook.create_sheet(title=sheet)
		workbook[sheet].append(title_columns)
		for num in range(ord('A'), ord('Z')):
			letter = chr(num)
			cell = workbook[sheet][f'{letter}1']
			cell.font = Font(bold=True)
		if len(sheets_info) == 1:
			workbook.active = workbook[sheet]  # only if amount of sheets is one
	try:
		workbook.remove(workbook["Sheet"])  # removing default sheet adding when workbook is creating
	except:
		pass
	return workbook


def sheet_get_params(file_type: str) -> dict:
	"""
	:param file_type: districts/managers
	:return: dict with params like {sheet_name: sheet_titles}
	"""
	folder_names = data.folder_names()
	if file_type == folder_names[0]:
		sheet_name = data.manager_main_sheet_name()
		title_columns = manager_subfile_columns_names()
	elif file_type == folder_names[1]:
		sheet_name = data.districts_main_sheet_name()
		title_columns = district_subfile_columns_names()
	return {
		sheet_name: title_columns
	}


def format_columns(workbook: Workbook, sheet_name: str) -> Workbook:
	worksheet = workbook[sheet_name]
	dims: dict = {}
	for row in worksheet.rows:
		for cell in row:
			if not cell.value is None:
				dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))
				alignment_obj = cell.alignment.copy(horizontal='center', vertical='center')
				cell.alignment = alignment_obj
	for col, value in dims.items():
		worksheet.column_dimensions[col].width = value + 5
	return workbook
