def ask_user(answer):
	while True:
        user_say = input('Как дела?')
       	if user_say == answer:
          	print('Это хорошо!')
           	break
ask_user('Хорошо')
