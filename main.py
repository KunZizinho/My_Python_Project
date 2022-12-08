import requests

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
print(x.headers)

        #  OR we can assignit to a variable and  do look thru dictionary (in Piyhon json file is considered a dictionary)

headers = x.headers
print(headers['X-Powered-By'])
print(headers.get('Content-Length', -1))

        # we can also do it as an if statement in case the web page does not have certain header it will return a message that the header does not exsist

if headers.get('Content-Length', None) is None:
    print("we couldn't figure out what the webpage is powered by.")

        # or we can do it thru try and catch 

try:
    print(headers['X-Powered-By'])
except Exception as e:
    print(f"Exception in getting header : {e}")  # f string helps us to formatstrings in py
print(headers.get('Content-Length', -1))




