dialog = {'hello': 'hi', 'how are you': 'fine', 'goodbye': 'ohh, donot leave me'}
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
			print('cya')
			break
		else:
			try:
				print(get_answer(user_say, dialog))
			except KeyError:
				print('%s' % 'hmm')
ask_user('Bye!')
#python ask_user_get_answer.py