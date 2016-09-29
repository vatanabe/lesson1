def ask_user(question, answer):
    while True:
        user_say = input(question)
        if user_say == answer:
            print('Это хорошо!')
            break
ask_user('Как дела? ', 'Хорошо')
