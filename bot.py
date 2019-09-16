import json

import requests
import misc
import parseManas
import weather
import lesson3

# https://api.telegram.org/bot720219419:AAGv4u2sDFt_VUuzZXDPh-rH2j4hJNAlLBE/sendmessage?chat_id=694174252&text=hi
token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    global last_update_id

    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        name = last_object['message']['from']['first_name'] + ' ' + last_object['message']['from']['last_name']
        try:
            message_text = last_object['message']['text']
        except:
            message_text = ''
        message = {
            'chat_id': chat_id,
            'message_text': message_text,
            'name': name
        }
        return message

    return None


def send_message(chat_id, text="Wait a second..."):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    words = get_updates()
    # with open('updates.json', 'w') as file:
    #     json.dump(words, file, indent=2, ensure_ascii=False)
    # get_message()
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            name = answer['name']
            asnwer = ['yemek', 'manasyemek', 'manas menu', 'еда', 'menu']

            if str(answer['message_text']).lower() in asnwer:
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
                    send_message(chat_id, result)
                except:
                    send_message(chat_id, 'Сегодня выходной')
            elif str(answer['message_text']).lower() == 'help':
                l = ''
                with open('help.txt', 'r') as text:
                    for line in text:
                        l += line + '\n'
                send_message(chat_id, l)
            elif str(answer['message_text']).lower() == 'weather':
                w = 'Данное время: ' + weather.weather_result['time'] + '\n' + 'Текушая температура: ' + \
                    weather.weather_result['temp_now'] + '\n' + 'Минимальная температура: ' + \
                    weather.weather_result['temp_min'] + '\n' + 'Максимальная температура: ' + weather.weather_result[
                        'temp_max'] + '\n' + \
                    'Влажность: ' + weather.weather_result['humidity'] + '\n' + \
                    'Ветер: ' + weather.weather_result['speed']
                send_message(chat_id, w)
            elif 'привет' in str(answer['message_text']).lower():
                send_message(chat_id, 'Здравствуйте,' + name + '!\n' + 'Напишите "help"')

            elif 'lesson_3' in str(answer['message_text']).lower():
                send_message(chat_id, lesson3.lesson_three())

        else:
            continue


if __name__ == '__main__':
    main()
