import warnings

from script.data import read_excel_file
from script.main import read_workers, write_files
from script import init_project_paths, config

from loguru import logger


def main():
	warnings.filterwarnings("ignore")
	logger.add(**config.LOGGING_PARAMS)
	init_project_paths()
	excel_file = read_excel_file()
	workers = read_workers(wb=excel_file)
	write_files(workers=workers)


if __name__ == '__main__':
	main()
