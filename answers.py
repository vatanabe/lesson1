dialog = {'привет': 'здрасте', 'как дела': 'хорошо', 'досвиданья': 'пока'}
def get_answer(key, dictinary):
	return dictinary[key]
def low_register(text):
	low=text.lower()
	low.replace('?','')
	low.replace('.','')
	low.replace(',','')
	low.replace('!','')
	low.replace(':','')
	low.replace(';','')
	low.replace('(','')
	low.replace(')','')
	return low.strip()
print(get_answer("привет", dialog))
print(get_answer("как дела", dialog))
print(low_register(' ПрИвет?.,:;()! '))
	#lower strip