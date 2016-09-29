name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name1 = name.pop()
while True:
	if name1 == "Валера":
		print('Валера нашелся')
		break
	else:
		name1 = name.pop()


