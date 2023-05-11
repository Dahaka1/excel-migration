from typing import Optional

from openpyxl.workbook import Workbook

from secondary_funcs.depricate import main_file_checking
from secondary_funcs.directories_init import init, init_secondary
from secondary_funcs.directories_init import init_district_folder
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


def create_excel(sheet_info: dict) -> Workbook:
	return create_excel_table(sheet_info)


def unpack_workers(workers_list) -> Optional[tuple]:
	return unpack(workers_list)


def sheet_params(excel_file_type: str) -> dict[str, list]:
	return sheet_get_params(excel_file_type)


def auto_format_columns(workbook: Workbook, sheet_name: str) -> Workbook:
	return format_columns(workbook, sheet_name)


def files_checking() -> bool:
	return main_file_checking()


def sub_folder_init(district) -> str:
	return init_district_folder(district)


def main_workbook() -> Workbook:
	return main_workbook_read()