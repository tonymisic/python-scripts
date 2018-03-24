import requests
import string

#returns a count of a single word
def count_words(st, word):
    count = str(st).count(word)
    return count

#returns a string
def get_text(URL):
    response = requests.get(URL)
    response.raise_for_status()
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print('Request Code invalid!')

#returns the list of all used words
def get_word_list(input_text):
    word_list = []
    input_text = input_text.replace('<', ' ')
    input_text = input_text.replace('>', ' ')

    #for i in range(len(input_text)):
     #   i = i
    return input_text


print(get_word_list(get_text("https://www.google.ca")))
