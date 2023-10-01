import keyboard


def initiate_action(action_description: str, button_chrs: str) -> bool:
	"""
	Нажатие горячей клавиши.
	"""
	print(action_description)
	while True:
		if keyboard.read_key().lower() in button_chrs:
			return True
		else:
			return False
