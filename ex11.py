list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while list:
	name = list.pop()
	if name == "Валера":
		print('Валера нашелся')
		break
	
