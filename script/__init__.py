import shutil
import os

from loguru import logger

from . import config
from .exceptions import RuntimeException
from .static.enums import ActionEnum


def init_project_paths(action: ActionEnum) -> str:
	"""
	Удаляет output папку, если она уже есть.
	Возвращает имя основного файла.
	"""
	if action == ActionEnum.SORT and os.path.exists(config.OUTPUT_PATH):
		shutil.rmtree(config.OUTPUT_PATH)
		logger.info(f"Существующая директория '{config.OUTPUT_PATH}' была удалена.")

	return init_main_file(action)


def init_main_file(action: ActionEnum) -> str:
	"""
	Определяет основной файл в директории.
	"""
	excel_files = list(str(file) for file in os.listdir() if file.endswith(".xlsx"))
	if not any(excel_files):
		raise RuntimeException("Not any .xlsx files found in project path")
	if len(excel_files) > 1:
		raise RuntimeException("Only one .xlsx file must be in script folder")

	main_filename = excel_files[0]

	if action == ActionEnum.SYNCHRONIZE:
		if not os.path.exists(config.OUTPUT_PATH):
			raise RuntimeException(f"'{config.OUTPUT_PATH}' folder not found. "
								   f"For data updating, firstly, you need to run main file sorting.")
		if not os.path.exists(f"{config.OUTPUT_PATH}/{main_filename}"):
			raise RuntimeException(f"Main file not found in {config.OUTPUT_PATH}. "
								   f"For data updating, firstly, you need to run main file sorting.")

	return main_filename


def confirm_action(action: ActionEnum) -> None:
	"""
	Подтверждение сноса текущих файлов =)
	"""
	if action == ActionEnum.SORT:
		if os.path.exists(config.OUTPUT_PATH):
			confirming = input(f"Подтвердите сортировку данных, еще раз введя '{ActionEnum.SORT.value}' "
							   f"(текущие файлы в папке '{config.OUTPUT_PATH}' будут удалены)\n")
			match ActionEnum(confirming):
				case ActionEnum.SORT:
					pass
				case _:
					exit(0)
