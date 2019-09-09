import requests

url = 'https://www.freeforexapi.com/api/live?pairs=EURUSD'

def func(i):
    r = requests.get(url)
    print(str(i) + ' - ' + str(r.status_code))
    print(r.json())


func(0)

'''
for i in range(1, 100):
    func(i)
'''
