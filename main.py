import os.path
from traceback import format_exc
import data
import main_funcs
import secondary_funcs

main_file_name, file_folder = data.config()


def main():
	main_funcs.copy()
	main_funcs.update()
	os.remove(main_file_name)


if __name__ == '__main__':
	try:
		secondary_funcs.main_directories_init()
		main()
		print("Сделано!\n"
			  f'Результат находится в папке "{file_folder}".\n'
			  'Резервная копия исходного файла - в "backup".')
	except:
		print(format_exc())
		print()
