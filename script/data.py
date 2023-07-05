import os
from typing import Iterable

import openpyxl
from openpyxl.cell import Cell
from openpyxl.styles import Alignment, Font, Protection
from openpyxl.worksheet.worksheet import Worksheet
from loguru import logger

from . import config


def read_excel_file() -> openpyxl.Workbook:
	"""
	Считывает файл в директории.
	"""
	for filename in os.listdir():
		if filename.endswith(".xlsx"):
			try:
				file: openpyxl.Workbook = openpyxl.load_workbook(filename=filename, data_only=True)
				main_file_name = filename
				if not all(
					(sheet in (str(sh).lower() for sh in file.sheetnames) for sheet in config.NEEDED_SHEETS.values())
				):
					raise RuntimeError("Not all searched sheets was founded.\n"
									   f"Searching for sheets: {list(config.NEEDED_SHEETS.values())}")
			except Exception as e:
				raise RuntimeError(f"Can't read the Excel file. Exception: ", e)
			break

	check_worksheets(file)
	cleaned_up_wb = cleanup_file_cells(wb=file)
	if not os.path.exists(config.OUTPUT_PATH):
		os.mkdir(config.OUTPUT_PATH)
	cleaned_up_wb.save(filename=f"{config.OUTPUT_PATH}/{main_file_name}")

	logger.info("Excel-файл обнаружен. Успешно произведена очистка от лишних символов в ячейках. "
		  f"Записан в папку '{config.OUTPUT_PATH}'.")

	return cleaned_up_wb


def check_worksheets(wb: openpyxl.Workbook) -> None:
	"""
	Проверяет листы на наличие столбцов, указанных в конфиге.
	"""
	main_worksheet: Worksheet = wb[config.NEEDED_SHEETS["MAIN_SHEET"]]
	secondary_worksheet: Worksheet = wb[config.NEEDED_SHEETS["SECONDARY_SHEET"]]

	def get_sheet_titles(sheet: Worksheet) -> Iterable[str]:
		sheet_titles_row = next(sheet.iter_rows())
		return (cell.value for cell in sheet_titles_row)

	def check_titles(columns: Iterable[str], searched_columns: Iterable[str], sheet_name: str) -> None:
		if any(
			(col not in searched_columns for col in tuple((str(item).strip() for item in columns)))
		):
			raise RuntimeError(f"Got an unexpected columns names in sheet '{sheet_name}'.\n"
							   f"Expected columns: {list(searched_columns)}")

	main_sheet_titles = get_sheet_titles(main_worksheet)
	secondary_sheet_titles = get_sheet_titles(secondary_worksheet)

	check_titles(
		columns=main_sheet_titles, searched_columns=config.MAIN_SHEET_COLUMNS.values(),
		sheet_name=config.NEEDED_SHEETS["MAIN_SHEET"]
	)
	check_titles(
		columns=secondary_sheet_titles, searched_columns=config.SECONDARY_SHEET_COLUMNS.values(),
		sheet_name=config.NEEDED_SHEETS["SECONDARY_SHEET"]
	)


def cleanup_file_cells(wb: openpyxl.Workbook) -> openpyxl.Workbook:
	"""
	На всякий случай удаляю лишние пробелы в ячейках.
	Можно добавить еще какое-нибудь другое форматирование.
	"""
	worksheets = wb.sheetnames
	for sheet in worksheets:
		ws = wb[sheet]
		for row in ws:
			for cell in row:
				if isinstance(cell.value, str):
					cell.value = cell.value.strip()
	return wb


def create_excel_file(sheet_name: str) -> openpyxl.Workbook:
	"""
	Создание Excel-файла
	"""
	wb = openpyxl.Workbook()
	sheet = wb.active
	sheet.title = sheet_name
	sheet.append(config.OUTPUT_FIELDS)
	return wb


def format_sheets(wb: openpyxl.Workbook, add_protection: bool) -> openpyxl.Workbook:
	"""
	Форматирование Excel-файла
	"""
	alignment = Alignment(horizontal="center", vertical="center")
	font_first_row = Font(bold=True, size=12)

	for sheet_name in wb.sheetnames:
		sheet: Worksheet = wb[sheet_name]
		first_row = next(sheet.iter_rows())

		if add_protection:
			sheet = add_sheet_protection(sheet, first_row)  # добавить защиту от изменений и валидацию данных

		for cell in first_row:
			cell.font = font_first_row  # добавить шрифт

		dims: dict = {}
		for row in sheet.rows:
			for cell in row:
				cell: Cell
				if cell.value:
					dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), len(str(cell.value))))

				cell.alignment = alignment  # выравнивание текста

		for col, value in dims.items():
			sheet.column_dimensions[col].width = value + 5  # изменить ширину столбцов

	return wb


def add_sheet_protection(ws: Worksheet, first_row: list[Cell]) -> Worksheet:
	"""
	Устанавливает защиту на изменение Excel-файла.
	Но делает возможными для редактирования столбцы, которые указаны как таковые в конфиге.
	"""
	not_protected_columns = []
	for cell in first_row:
		try:
			cell_alias = next(key for key, val in config.MAIN_SHEET_COLUMNS.items() if val == cell.value)
			if cell_alias in config.PROTECTION_SHEETS_PARAMS["NOT_PROTECTED_COLUMNS"]:
				not_protected_columns.append(cell.column_letter)  # определяю столбцы, которые можно редактировать
		except StopIteration:
			continue  # в Output fields есть другие столбцы. Потом мб нужно будет поправить костыль.

	ws.protection.sheet = True

	for row in ws:
		for cell in row:
			cell: Cell
			if cell.column_letter in not_protected_columns:
				cell.protection = Protection(locked=False)
	return ws
