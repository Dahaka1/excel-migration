from __future__ import annotations

import datetime
import os
from typing import Iterable

from openpyxl.worksheet.worksheet import Worksheet

from . import config
from .data import create_excel_file, format_sheets
from .exceptions import AttributeException, ValueException, RuntimeException


class Worker:
	"""
	Класс работника
	"""
	def __init__(self, **kwargs):
		if any(
			(col not in kwargs for col in config.MAIN_SHEET_COLUMNS.values())
		):
			raise AttributeException(f"Didn't get some column value.\n"
								 f"Needed columns: {list(config.MAIN_SHEET_COLUMNS.values())}")

		self.district: str = kwargs.get(config.MAIN_SHEET_COLUMNS["DISTRICT_COLUMN"]) or config.NULL_VALUE
		self.name: str = kwargs.get(config.MAIN_SHEET_COLUMNS["EMPLOYEE_COLUMN"]) or config.NULL_VALUE
		self.working_position: str = kwargs.get(config.MAIN_SHEET_COLUMNS["WORKING_POSITION_COLUMN"]) or config.NULL_VALUE
		self.manager_name: str = kwargs.get(config.MAIN_SHEET_COLUMNS["MANAGER_COLUMN"]) or config.NULL_VALUE
		self.paying_period: str = kwargs.get(config.MAIN_SHEET_COLUMNS["PAYING_PERIOD"]) or config.NULL_VALUE
		self.paying_amount: str = kwargs.get(config.MAIN_SHEET_COLUMNS["PAYING_AMOUNT"]) or config.NULL_VALUE

		# self.paying_date: str | None = None


class WorkingPosition:
	"""
	Класс должности с определенными датами выплат.
	Kwargs - месяцы с указанной или не указанной датой выплаты.
	"""
	def __init__(self, name: str, **kwargs):
		months_and_payments_dates_dict = {key.lower(): val for key, val in kwargs.items() if key.lower() in config.MONTHS}

		if not all(
			(month in months_and_payments_dates_dict for month in config.MONTHS)
		):
			raise AttributeException("Not all working position months data was received")

		self.name = name
		self.months = months_and_payments_dates_dict

	def __getitem__(self, item: str) -> datetime.datetime:
		"""
		Возвращает дату выплаты по указанному месяцу.
		"""
		if item not in self.months:
			raise AttributeException(f"Getitem only receives month name.")
		return self.months.get(item)


class Manager:
	"""
	Класс менеджера
	"""
	def __init__(self, name: str | None, business_unit: str):
		self.name = name or config.NULL_VALUE
		self.workers: list[Worker] | None = None
		self.business_unit = business_unit
		self.last_name = name.split()[0]

	def add_workers(self, *args) -> None:
		"""
		Определяет сотрудников менеджера
		"""
		if not all(
			(worker.manager_name == self.name for worker in args)
		):
			raise ValueException(f"Manager {self.name} got an non-self workers")
		args = sorted(args, key=lambda worker: worker.name)
		self.workers = []
		self.workers.extend(args)

	def write_file(self, output_dir: str) -> int:
		"""
		Создает файл о сотрудниках, определенных менеджером.

		Возвращает количество строк, записанных в файл.
		"""
		if not any(self.workers):
			raise RuntimeException(f"Not any workers was defined for manager {self.name}")

		sheet_name = config.MANAGER_AND_DISTRICTS_MAIN_SHEET_NAME % self.last_name
		wb = create_excel_file(sheet_name=sheet_name)
		ws: Worksheet = wb.active

		written_workers = 0

		for worker in self.workers:
			idx = self.workers.index(worker) + 1
			ws.append(
				[idx, self.business_unit, worker.name, worker.working_position,
				self.name, worker.paying_period, worker.paying_amount]
			)
			written_workers += 1

		fileout_path = f"{output_dir}/{self.name}.xlsx"
		if not os.path.exists(f"{output_dir}"):
			os.mkdir(output_dir)
		wb = format_sheets(wb=wb, add_protection_and_validation=True)
		wb.save(filename=fileout_path)

		return len(self.workers)

	@staticmethod
	def write_districts_files(managers: list[Manager], workers: Iterable[Worker]) -> int:
		"""
		Создает общие файлы по регионам.

		Все менеджеры должны быть с определенными работниками!

		Возвращает количество строк, записанных в файл.
		"""
		if any(
			(not any(manager.workers) for manager in managers)
		):
			raise ValueException(f"Not all managers has defined workers")
		districts_names = set((manager.business_unit for manager in managers))

		written_workers = 0

		for district_name in districts_names:
			if district_name != config.NULL_VALUE:
				output_dir = f"{config.OUTPUT_PATH}/{district_name}"
				if not os.path.exists(output_dir):
					os.mkdir(output_dir)
			else:
				output_dir = config.OUTPUT_PATH
			fileout_path = f"{output_dir}/{district_name}.xlsx"
			sheet_name = config.MANAGER_AND_DISTRICTS_MAIN_SHEET_NAME % district_name
			wb = create_excel_file(sheet_name=sheet_name)
			ws: Worksheet = wb.active
			district_workers = list(filter(lambda w: w.district == district_name, workers))
			for worker in district_workers:
				idx = district_workers.index(worker) + 1
				ws.append(
					[idx, district_name, worker.name, worker.working_position,
					 worker.manager_name, worker.paying_period, worker.paying_amount]
				)
				written_workers += 1
			wb = format_sheets(wb=wb, add_protection_and_validation=False)
			wb.save(filename=fileout_path)

		return written_workers
