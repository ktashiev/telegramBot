import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_html(url):
    response = requests.get(url)
    return response.text


def get_info_course_three(html):
    week = datetime.today().weekday()
    soup = BeautifulSoup(html, 'lxml')
    time = datetime.now().time()
    time_now = str(time.hour) + ":" + str(time.minute)
    # time_now = '11:30'
    help = ''
    second = ''
    times_html = soup.find('div', class_='.container-fluid').find('table',
                                                                  class_='table table-bordered').find_all('tr')
    for i in times_html:
        try:
            if datetime.strptime(time_now, '%H:%M').time() <= datetime.strptime(str(i.next.next).split('-')[0],
                                                                                '%H:%M').time():
                help = i.find_all()[week].next + '\n'
                second = i.find_all()[week + 1].next + '\n' + i.find_all()[
                    week + 2].next + '\n' + i.find_all()[
                             week + 3].next + '\n' + i.find_all()[week + 4].next
                break
        except:
            continue
    if second:
        second = 'Reserved'
    if help:
        help = ''
    return help + second


def lesson_three(url):
    result = get_info_course_three(get_html(url))
    return result


if __name__ == '__main__':
    lesson_three()
