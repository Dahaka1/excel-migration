import warnings

from script.data import prepare_excel_file, read_excel_file
from script.sorting import read_workers, write_files
from script import init_project_paths, config, confirm_action
from script.static.enums import ActionEnum
from script.exceptions import ValueException
from script.synchronizing import update_workers_paying_amount

from loguru import logger


def main():
	warnings.filterwarnings("ignore")
	logger.add(**config.LOGGING_PARAMS)
	action_number = input("Введите:\n"
				   f"{ActionEnum.SORT.value} - сортировка данных на основе исходного файла\n"
				   f"{ActionEnum.SYNCHRONIZE.value} - сбор данных из побочных файлов в основной\n")
	action = ActionEnum(action_number)
	confirm_action(action)
	main_filename = init_project_paths(action)
	match action:
		case ActionEnum.SORT:
			excel_file = prepare_excel_file(main_filename)
			workers = read_workers(wb=excel_file)
			write_files(workers=workers)
		case ActionEnum.SYNCHRONIZE:
			excel_file = read_excel_file(f"{config.OUTPUT_PATH}/{main_filename}")
			workers = read_workers(wb=excel_file)
			update_workers_paying_amount(workers, excel_file, main_filename)
		case _:
			raise ValueException("Incorrect action number")


if __name__ == '__main__':
	main()
	input("\nНажмите \"Enter\", чтобы выйти ")
