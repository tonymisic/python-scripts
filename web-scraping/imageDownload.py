import requests, bs4, os
url = 'https://scs.ryerson.ca/~tmisic/lab2/main.html'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
element = soup.select('img')
if element == []:
    print('No images found.')
else:
    tmp = url.split('/')
    tmp = tmp[:-1]
    imageUrl = ''
    for i in range(len(tmp)):
        imageUrl = imageUrl + tmp[i] + '/'
    imageUrl = imageUrl + element[0].get('src')
    print('Downloading from ' + imageUrl)
    imageFile = open('image.png', 'wb')
    res = requests.get(imageUrl)
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print('Download complete.')