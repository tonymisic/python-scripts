import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()
playFile = open('RandJ.txt', 'wb')
for chunk in response.iter_content(100000):
    playFile.write(chunk)
playFile.close()
