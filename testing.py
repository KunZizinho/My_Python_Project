import requests
from bs4 import BeautifulSoup

# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)
# print(x.headers)

        #  OR we can assignit to a variable and  do look thru dictionary (in Piyhon json file is considered a dictionary)

# headers = x.headers
# print(headers['X-Powered-By'])
# print(headers.get('Content-Length', -1))

        # we can also do it as an if statement in case the web page does not have certain header it will return a message that the header does not exsist

# if headers.get('Content-Length', None) is None:
#     print("we couldn't figure out what the webpage is powered by.")

        # or we can do it thru try and catch 

# try:
#     print(headers['X-Powered-By'])
# except Exception as e:
    # print(f"Exception in getting header : {e}")  # f string helps us to formatstrings in py
# print(headers.get('Content-Length', -1))

        #  helpful things to consider  is that thru developer tools we cal locate get req and copy it then go to curl trillworks which converts our copied request to the language we need it in
print()
print()
print("Apple headers scrapped")
print()
print()

cookies = {
    'geo': 'US',
    's_fid': '3E2CE2C35AE1B89E-0F3046A59751C758',
    's_cc': 'true',
    'mk_epub': '%7B%22btuid%22%3A%221czcpsg%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
}

headers = {
    'authority': 'www.apple.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'geo=US; s_fid=3E2CE2C35AE1B89E-0F3046A59751C758; s_cc=true; mk_epub=%7B%22btuid%22%3A%221czcpsg%22%2C%22prop57%22%3A%22www.us.homepage%22%7D',
    'referer': 'https://duckduckgo.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
# response = requests.get('https://www.apple.com/', cookies=cookies, headers=headers)
# appleHeaders = response.headers
# print(f"headers : {appleHeaders}")

        #  PARSING WITH BEUTIFULSOUP    

        #  our target url
url = 'https://www.apple.com/'
# urls = ['https://www.apple.com/', 'https://realpython.com/', 'https://stackoverflow.com/', 'https://github.com/']

        # we have to create our request instance
req = requests.get(url)

        # using BS module to parse html
soup = BeautifulSoup(req.text, 'html.parser')

print("Title of webpage is : ")
for title in soup.find_all('title'):
    print(title.get_text())

print()
print('Continuing with Apple webpage for testing purposes. --Line 79')
print()
print()

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
headers = response.headers
print(f"title : {soup.title.string}")
# print(f"headers : {headers}")

try:
    print(headers['X-Powered-By'])
except Exception as e:
    print(f"Exception in getting header : {e}")
print(headers.get('Content-Length', -1))
if headers.get('Content-Length', None) is None:
    print("we couldn't figure out what the webpage is powered by.")

print()
print(' --Line 99')
print()
print()

urls = ['https://www.apple.com', 'https://www.google.com', 'https://www.youtube.com']

for url in urls:
    print(f"URL : {url}\n")
    try:
        response = requests.get(url, cookies=cookies, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = response.headers
        print(f"title : {soup.title.string}")
        # print(f"headers : {headers}")
        print(headers['X-Powered-By'])
    except Exception as e:
        print(f"Exception in getting header : {e}")
    print(headers.get('Content-Length', -1))
    if headers.get('Content-Length', None) is None:
        print("we couldn't figure out what the webpage is powered by.")

    # Reading a csv file

# with open("top-100.csv", "r") as f:
    # data = f.read()
# lines = data.split("\n")
# print('---line 124 start---', data, '\n---line 124 end---')
# print('-------------------------125 start-----------------', lines, '-------------------------125 end-----------------\n', len(lines))

# for line in lines:
    # url = "https://"+line.split(",")[1]
    # print('--------line 130-----')
    # print(line.split(",")[1])
    # print()
    # try:
        # response = requests.get(url, cookies=cookies, headers=headers, timeout=5)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # headers = response.headers
        # print(f"title : {soup.title.string}\n")
        # print(f"headers : {headers}")
        # print(headers['X-Powered-By'])
    # except Exception as e:
    #     print(f"Exception in getting header : {e}")
print('-----------------line 144-------------')

with open("top-100.csv", "r") as f:
    # data1M = f.read()
    data = f.read()
# lines = data1M.split("\n")
lines = data.split("\n")
print(lines, '--------------------------------------147 end\n')

uniqueURLS = {}
allURLS = []
for line in lines:
    url = "https://"+line.split(",")[1]
    # print(f"URL : {url}\n")
    uniqueURLS = True
    allURLS.append(url)
print(f"Length : len(lines) {len(lines)} | len(allURLS) : {len(allURLS)}")
print(lines, '\n', allURLS, '\n')