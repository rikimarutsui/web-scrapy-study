import requests

response = requests.get('http://www.hko.gov.hk')

print('Response Status: ', response.status_code)
print('Response Header: ', response.headers['content-type'])
print('Response Encoding: ', response.encoding)
print('Response Content: ', response.text[:100], '...')
