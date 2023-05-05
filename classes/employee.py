from datetime import date
from typing import Optional, Any

from data.additional_info import months


class WorkingPosition:
	def __init__(
		self,
		name: str,
		worksheet: Any
	):
		self.worksheet = worksheet

		self.name = name
		self.excel_file_row_number: Optional[int] = self.find_row()
		self.updating_date: Optional[date] = self.find_updating_date() if not self.excel_file_row_number is None else None

	def find_updating_date(self) -> Optional[date]:
		current_month = months()[date.today().month]
		columns = range(ord("G"), ord("S"))
		months_columns = [f'{chr(i)}' for i in columns]
		current_column = None
		for column in months_columns:
			month_name = self.worksheet[f'{column}1'].value
			if month_name == current_month:
				current_column = column
		if current_column:
			updating_date = self.worksheet[f'{current_column}{self.excel_file_row_number}'].value
			if not updating_date is None:
				return updating_date.date()
			else:
				return None
		raise ValueError("Ошибка: не найден текущий месяц в основной таблице!")

	def find_row(self) -> Optional[int]:
		current_column = 'A'
		test_list = []
		for row in range(1, len(list(self.worksheet.rows))):
			working_position_name = self.worksheet[f"{current_column}{row}"].value
			test_list.append(working_position_name)
			if working_position_name == self.name:
				return row
		return None


class Worker:
	def __init__(
		self,
		fullname: str,
		workers_worksheet: Any,
		positions_worksheet: Any
	):
		self.worksheets = (
			workers_worksheet,
			positions_worksheet
		)

		self.fullname = fullname
		self.excel_file_row_number = self.find_row()
		self.district, self.working_position, self.manager_name = self.find_params()
		self.updating_date: date = self.working_position.updating_date

	def find_row(self):
		current_column = "B"
		counter = 2
		while True:
			worker_name = self.worksheets[0][f"{current_column}{counter}"].value
			if not worker_name is None:
				if worker_name == self.fullname:
					return counter
				else:
					counter += 1
					continue
			else:
				raise StopIteration(f"Ошибка: на найден сотрудник {self.fullname} в основной таблице!")

	def find_params(self) -> tuple:
		district, working_position, manager = \
			[self.worksheets[0][f"{col}{self.excel_file_row_number}"].value for col in ["A", "C", "E"]]
		return district, WorkingPosition(name=working_position, worksheet=self.worksheets[1]), manager
