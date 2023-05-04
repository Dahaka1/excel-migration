from secondary_funcs.directories_init import init, init_secondary
from secondary_funcs.read_employees import find_workers
from secondary_funcs.read_excel import *
from secondary_funcs.unpacking import unpack
from secondary_funcs.write_excel import *
from secondary_funcs.deprecate import main_file_checking


def read_main_file(sheet_name: str) -> Any:
	return read_file(sheet_name)


def read_secondary_file(filepath) -> Any:
	return read_subfile(filepath)


def find_all_workers() -> list:
	return find_workers()


def main_directories_init() -> NoReturn:
	return init()


def secondary_directories_init(path) -> NoReturn:
	return init_secondary(path)


def create_excel(sheet_info: dict):
	return create_excel_table(sheet_info)


def unpack_workers(workers_list) -> tuple:
	return unpack(workers_list)


def sheet_params(excel_file_type: str) -> dict:
	return sheet_get_params(excel_file_type)


def auto_format_columns(workbook: Any, sheet_name: str) -> Any:
	return format_columns(workbook, sheet_name)


def files_checking():
	return main_file_checking()