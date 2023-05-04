from traceback import format_exc

import data
import main_funcs
import secondary_funcs


def main():
	main_funcs.copy()
	main_funcs.update()


if __name__ == '__main__':
	file_folder = data.config()[1]
	try:
		secondary_funcs.main_directories_init()
		main()
		print("Сделано!\n"
			  f'Результат находится в папке "{file_folder}".\n'
			  'Резервная копия исходного файла - в "backup".')
	except:
		print(format_exc())
