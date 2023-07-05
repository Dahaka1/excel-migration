import shutil
import os

from . import config


def init_project_paths() -> None:
	if os.path.exists(config.OUTPUT_PATH):
		shutil.rmtree(config.OUTPUT_PATH)
