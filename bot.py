import requests
import misc
import parseManas

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
        message_text = last_object['message']['text']
        message = {
            'chat_id': chat_id,
            'message_text': message_text
        }
        return message

    return None


def send_message(chat_id, text="Wait a second..."):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # words = get_updates()
    # with open('updates.json', 'w') as file:
    #     json.dump(words, file, indent=2, ensure_ascii=False)

    # get_message()
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            asnwer = ['yemek', 'manasyemek', 'manas menu', 'еда', 'menu']

            if str(answer['message_text']).lower() in asnwer:
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
            elif str(answer['message_text']).lower() == 'help':
                l = ''
                with open('help.txt', 'r') as text:
                    for line in text:
                        l += line + '\n'
                send_message(chat_id, l)
        else:
            continue


if __name__ == '__main__':
    main()
