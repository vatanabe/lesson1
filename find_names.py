name = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
find_name = input('Введите искомое имя: ')
def  find_person(name1, list):
	name2 = name.pop()
	while True:
		if name2 == name1:
			print('%s нашелся' % name1)
			break
		else:
			name2 = name.pop()
find_person(find_name, name)
