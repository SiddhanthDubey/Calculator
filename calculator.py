import back_end

while True:
		text = input('Calculator : ')
		result, error = back_end.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)