from email import message
import telebot

is_writed = {}

bot = telebot.TeleBot('5373930444:AAFRizpv1iKV7_DVSxqbSeGV1PwfhSeaCXE')

@bot.message_handler(commands=['start'])
def start_message(message):
    is_writed[message.from_user.id] = 0
    bot.send_message(message.chat.id, 'Здравствуйте, как вас зовут?')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.find("транспорт") == -1:
        if is_writed[message.from_user.id] == 0:
            is_writed[message.from_user.id] = 1
            bot.send_message(message.chat.id, 'Здравствуйте, ' + message.text + '. Напишите ваше обращение')
        elif is_writed[message.from_user.id] == 1:
            bot.send_message(message.chat.id, 'Готово!')
            is_writed[message.from_user.id] = message.text
            bot.send_message(795310679, "Новое обращение: \n " + message.text)
        elif is_writed[message.from_user.id] != 1 and is_writed[message.from_user.id] != 0:
            bot.send_message(message.chat.id, 'Вы уже отправили обращение. Наша команда его просмотрит')
            


bot.polling(none_stop=True, interval=0)