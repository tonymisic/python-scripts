import requests
import bs4
import requests
import string


def get_links(soup):
    elements = soup.select('div')
    result = []
    for i in range(len(elements)):
        element = soup.select('div')[i]
        link = element.get('src')
        result.append(link)
    return result


def count_words(input_text, word):
    count = str(input_text).count(word)
    return count


def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == requests.codes.ok:
        return bs4.BeautifulSoup(response.text, "html.parser")
    else:
        print('Request Code invalid!')


def list_print(in_list):
    for i in range(len(in_list)):
        print(in_list[i])


list_print(get_links(get_soup("https://www.youtube.com/watch?v=PhB_wEBVvaA")))


