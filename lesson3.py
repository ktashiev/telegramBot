import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def get_html(url):
    response = requests.get(url)
    return response.text


def get_info_course_three(html):
    week = datetime.today().weekday()
    soup = BeautifulSoup(html, 'lxml')
    time = (datetime.now() + timedelta(hours=6)).time()
    time_now = str(time.hour) + ":" + str(time.minute)
    help = ''
    times_html = soup.find('div', class_='.container-fluid').find('table',
                                                                  class_='table table-bordered').find_all('tr')
    for i in times_html:
        try:
            if datetime.strptime(time_now, '%H:%M').time() <= datetime.strptime(str(i.next.next).split('-')[0],
                                                                                '%H:%M').time():

                if i.find_all('td')[week + 1].find('div') == ' Ayrılmış (Reserved)':
                    continue
                if i.find_all('td')[week + 1].find('div') == None:
                    continue
                if i.find_all()[0].next in ' #':
                    continue
                else:
                    help += i.find_all()[0].next + '\n'
                a = i.find_all('td')[week + 1].find('div')

                help += a.next + '\n' + a.next.next.next + '\n' + a.next.next.next.next.next + '\n' + '\n'
        except:
            continue
    return help


def lesson_three(url):
    if get_info_course_three(get_html(url)):
        result = get_info_course_three(get_html(url))
    else:
        result = 'Reserved'
    return result


if __name__ == '__main__':
    lesson_three('http://timetable.manas.edu.kg/department-printer/95')
