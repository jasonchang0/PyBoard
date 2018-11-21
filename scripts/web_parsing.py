from urllib import request, parse
import re

url = 'http://pythonprogramming.net'
parameters = {'s': 'basic', 'submit': 'search'}

data = parse.urlencode(parameters)
data = data.encode('utf-8')

req = request.Request(url, data)
resp = request.urlopen(req)

respData = resp.read()
# print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for paragraph in paragraphs:
    print(paragraph)
