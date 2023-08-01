import keyboard


def initiate_action(action_description: str, button_chr: str) -> bool:
	"""
	Нажатие горячей клавиши.
	"""
	if len(button_chr) > 1:
		raise ValueError("Invalid hotkey")
	print(action_description)
	while True:
		if keyboard.read_key() == button_chr:
			return True
		else:
			return False
