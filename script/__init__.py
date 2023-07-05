import shutil
import os

from . import config

from loguru import logger


def init_project_paths() -> None:
	"""
	Удаляет output папку, если она уже есть.
	"""
	if os.path.exists(config.OUTPUT_PATH):
		shutil.rmtree(config.OUTPUT_PATH)
		logger.info(f"Существующая директория '{config.OUTPUT_PATH}' была удалена.")

	check_files_exists()


def check_files_exists() -> None:
	"""
	Проверяет, есть ли в директории файл(-ы) xlsx.
	"""
	if not any(
		(str(file).endswith(".xlsx") for file in os.listdir())
	):
		raise RuntimeError("Not any .xlsx files found in project path")
