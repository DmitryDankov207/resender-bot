import telebot

bot = telebot.TeleBot('973774765:AAE-fnENcQ4qygcdQjqUGGmvz6QWE8SBCl0')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет')

#@bot.message_handler(content_types=['text'])
#def send_text(message):
#    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['get_id'])
def start_message(message):
    bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=['resend_to'])
def start_message(message):
    chat_id = message.text.split(' ')[1]
    bot.send_message(message.chat.id, message.text.split(' ')[2] +'\n' + str(message.chat.id))

@bot.message_handler(content_types=['text', 'document', 'audio'])
def start_message(message):
    if message.from_user.first_name.contains("Полина"):
        bot.send_message(message.chat.id, "шууэээээд")


bot.polling()
