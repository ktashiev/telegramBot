import telebot
import weather
import lesson3
import parseManas
from datetime import datetime

bot = telebot.TeleBot('720219419:AAGv4u2sDFt_VUuzZXDPh-rH2j4hJNAlLBE')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.resize_keyboard = 5
keyboard1.row('yemek', 'weather')
keyboard1.row('course1', 'course2')
keyboard1.row('course3', 'course4')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я готов ответить на ваши вопросы', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    lesson_1 = 'http://timetable.manas.edu.kg/department-printer/1'
    lesson_2 = 'http://timetable.manas.edu.kg/department-printer/48'
    lesson_3 = 'http://timetable.manas.edu.kg/department-printer/95'
    lesson_4 = 'http://timetable.manas.edu.kg/department-printer/142'

    if message.text.lower() == 'help':
        l = ''
        with open('help.txt', 'r') as text:
            for line in text:
                l += line + '\n'
        bot.send_message(message.chat.id, l + str(datetime.now()))
    elif message.text.lower() == 'weather':
        w = 'Данное время: ' + weather.weather_result['time'] + '\n' + 'Текушая температура: ' + \
            weather.weather_result['temp_now'] + '\n' + 'Минимальная температура: ' + \
            weather.weather_result['temp_min'] + '\n' + 'Максимальная температура: ' + weather.weather_result[
                'temp_max'] + '\n' + \
            'Влажность: ' + weather.weather_result['humidity'] + '\n' + \
            'Ветер: ' + weather.weather_result['speed']
        bot.send_message(message.chat.id, w)

    elif message.text.lower() == 'course1':
        bot.send_message(message.chat.id, lesson3.lesson_three(lesson_1))
    elif message.text.lower() == 'course2':
        bot.send_message(message.chat.id, lesson3.lesson_three(lesson_2))
    elif message.text.lower() == 'course3':
        bot.send_message(message.chat.id, lesson3.lesson_three(lesson_3))
    elif message.text.lower() == 'course4':
        bot.send_message(message.chat.id, lesson3.lesson_three(lesson_4))
    elif message.text.lower() == 'yemek':
        try:
            all_result = parseManas.index()
            result = all_result['yemek1'] + ' - ' + all_result['kalori1'] + ' калорий\n' + all_result[
                'yemek2'] + ' - ' + \
                     all_result[
                         'kalori2'] + ' калорий\n' + \
                     all_result['yemek3'] + ' - ' + all_result['kalori3'] + ' калорий\n' + all_result[
                         'yemek4'] + ' - ' + \
                     all_result[
                         'kalori4'] + ' калорий'
            bot.send_message(message.chat.id, result)
        except:
            bot.send_message(message.chat.id, 'Сегодня выходной')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADxgEAAsoDBguh9vhwm5TPHRYE')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
