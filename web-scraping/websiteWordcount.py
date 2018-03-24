import requests, webbrowser, os, sys, re

response = requests.get('')
def countWord(string, word):
    count = str(string).count(word)
    return count

response.raise_for_status()
if response.status_code == requests.codes.ok:
    inputText = response.text
    wrdList = []
    print('Count of Words used:')
    for i in range(len(wrdList)):
        print(wrdList[i].title() + ': ' + str(countWord(inputText, wrdList[i])))
else:
    print('Request not available')