from loguru import logger


class Error(Exception):
	def __init__(self, content: str):
		logger.error(f"<{self.__class__.__name__}>: {content}")
		super().__init__(content)


class StdException(Error):
	pass


class RuntimeException(Error):
	pass


class AttributeException(Error):
	pass


class ValueException(Error):
	pass
