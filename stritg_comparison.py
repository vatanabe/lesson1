def comparison(str1, str2):
	str3='learn'
	if str1 == str2:
		return 1
	elif str1 != str2 and len(str1) > len(str2) and str2 != str3:
		return 2
	elif str1 != str2 and str2 == str3:
		return 3
word1 = input('Введите строку: ')
word2 = input('Введите вторую строку: ')
print(comparison(word1, word2))