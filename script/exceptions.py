from loguru import logger


class Error(Exception):
	def __init__(self, content: str):
		logger.error(f"<{self.__class__.__name__}>: {content}")
		input("Press \"Enter\" to exit ")
		exit(0)


class StdException(Error):
	pass


class RuntimeException(Error):
	pass


class AttributeException(Error):
	pass


class ValueException(Error):
	pass
