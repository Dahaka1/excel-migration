import os.path
from shutil import copy2, rmtree

import data

main_file_name, file_path = data.config()


def copy_files():
	def del_folder(folder_name):
		if os.path.exists(folder_name):
			rmtree(folder_name)

	def copy_file(folder):
		if not os.path.exists(folder):
			os.mkdir(folder)
		copy2(main_file_name, f'{folder}/{main_file_name}')
	if os.path.exists(main_file_name):
		del_folder('backup')
		del_folder(file_path)
		copy_file('backup')
		copy_file(file_path)
	else:
		raise FileNotFoundError('Исходный файл не найден! Он должен быть в директории со скриптом, называться "Список '
								'сотрудников" и иметь тип Excel-файла (.xlsx).')
