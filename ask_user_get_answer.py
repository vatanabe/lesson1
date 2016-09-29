dialog = {'привет': 'здрасте', 'как дела': 'хорошо', 'досвиданья': 'пока'}
def get_answer(key, dictinary):
	punctuation = ['?', ',', '.', ';', ':', '!', '(', ')']
	for sign in punctuation:
		key = key.replace(sign,'')
	key = key.strip()
	key = key.lower()
	return dictinary[key]
def ask_user(answer):
	while True:
		user_say = input()
		if user_say == answer:
			print('Ну пока...')
			break
		else:
			print(get_answer(user_say, dialog))
ask_user('Пока!')
#ask_user_get_answer.py