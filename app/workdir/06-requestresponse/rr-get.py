import requests

#response = requests.get('https://ithelp.ithome.com.tw/search?search=python&tab=question')
#print(response)

payload = {
    'search': 'python',
    'tab': 'question'
}
response = requests.get('https://ithelp.ithome.com.tw/search', params=payload)
print(response.url)