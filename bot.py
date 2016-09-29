from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
	print('Вызван /start')
	bot.sendMessage(update.message.chat_id, text='Hi brother!')


def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def rut_bot():
	updater = Updater("277846833:AAGKlSQ1vpbG_a1s_6W3f464X5FAo_VZbY8")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	rut_bot()