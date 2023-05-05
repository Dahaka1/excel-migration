from typing import Optional

from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from secondary_funcs.depricate import main_file_checking
from secondary_funcs.directories_init import init, init_secondary
from secondary_funcs.read_employees import find_workers
from secondary_funcs.read_excel import *
from secondary_funcs.unpacking import unpack
from secondary_funcs.write_excel import *


def read_main_file(sheet_name: str) -> Worksheet:
	return read_file(sheet_name)


def read_secondary_file(filepath) -> Workbook:
	return read_subfile(filepath)


def find_all_workers() -> Optional[list]:
	return find_workers()


def main_directories_init() -> None:
	return init()


def secondary_directories_init(path) -> None:
	return init_secondary(path)


def create_excel(sheet_info: dict):
	return create_excel_table(sheet_info)


def unpack_workers(workers_list) -> Optional[tuple]:
	return unpack(workers_list)


def sheet_params(excel_file_type: str) -> dict:
	return sheet_get_params(excel_file_type)


def auto_format_columns(workbook: Workbook, sheet_name: str) -> Workbook:
	return format_columns(workbook, sheet_name)


def files_checking():
	return main_file_checking()
