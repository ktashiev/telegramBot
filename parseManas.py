import requests
from bs4 import BeautifulSoup

list_photo = {}
list_link = []


def get_html(url):
    response = requests.get(url)
    return response.text


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    food = soup.find('table').find('tr', bgcolor='#b7d2f2').find_all('a')
    kalories = soup.find('table').find('tr', bgcolor='#b7d2f2').find_all('b')
    yemek1 = food[0].next
    y1 = str(yemek1).replace('Ä±', 'ı').replace('Ã', 'Ç').replace('Å', 'ş').replace('Ã¶', 'ö').replace('Ã§',
                                                                                                         'ç').replace(
        'Ä', 'ğ').replace('Ã¼', 'ü').replace('Å', 'Ş')

    yemek2 = food[1].next
    y2 = str(yemek2).replace('Ä±', 'ı').replace('Ã', 'Ç').replace('Å', 'ş').replace('Ã¶', 'ö').replace('Ã§',
                                                                                                         'ç').replace(
        'Ä', 'ğ').replace('Ã¼', 'ü').replace('Å', 'Ş')

    yemek3 = food[2].next
    y3 = str(yemek3).replace('Ä±', 'ı').replace('Ã', 'Ç').replace('Å', 'ş').replace('Ã¶', 'ö').replace('Ã§',
                                                                                                         'ç').replace(
        'Ä', 'ğ').replace('Ã¼', 'ü').replace('Å', 'Ş')

    yemek4 = food[3].next
    y4 = str(yemek4).replace('Ä±', 'ı').replace('Ã', 'Ç').replace('Å', 'ş').replace('Ã¶', 'ö').replace('Ã§',
                                                                                                         'ç').replace(
        'Ä', 'ğ').replace('Ã¼', 'ü').replace('Å', 'Ş')

    kalori1 = kalories[2].next
    kalori2 = kalories[4].next
    kalori3 = kalories[6].next
    kalori4 = kalories[8].next

    for i in range(4):
        list_link.append(food[i].get('href'))
    foods_today = {
        'yemek1': y1,
        'yemek2': y2,
        'yemek3': y3,
        'yemek4': y4,
        'kalori1': kalori1,
        'kalori2': kalori2,
        'kalori3': kalori3,
        'kalori4': kalori4,
    }
    return foods_today


# def get_all_photos(html):
#     soup = BeautifulSoup(html, 'lxml')
#     photos = soup.find('div', id='res').find('div', id='search').find('div').find('td').find('img').get('src')
#     return photos


def index():
    url = 'http://bis.manas.edu.kg/menu/'
    all_links = get_all_links(get_html(url))
    return all_links


if __name__ == '__main__':
    index()
