dialog = {'привет': 'здрасте', 'как дела': 'хорошо', 'досвиданья': 'пока'}
def get_answer(key, dictinary):
	key = key.lower()
	key = key.replace('?','')
	key = key.replace('.','')
	key = key.replace(',','')
	key = key.replace('!','')
	key = key.replace(':','')
	key = key.replace(';','')
	key = key.replace('(','')
	key = key.replace(')','')
	key = key.strip()
	return dictinary[key]
print(get_answer(" ПривеТ", dialog))
