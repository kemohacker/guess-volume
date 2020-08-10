import requests
dictionary = open('/root/Desktop/dictionary.txt','r')
url = input('Please enter a URL:')
for x in dictionary:
    r = requests.get(url +"/" + x.rstrip('/n'))
    if r.status_code == 200:
        print('the page'+ url + '/' +x+ 'is available')
    else:
        print('the page' +url + '/' +x+ 'is not available')
