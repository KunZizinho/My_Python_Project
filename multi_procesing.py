import requests
from bs4 import BeautifulSoup
import tldextract
import time
import requests
from multiprocessing import Process, Queue

def worker(input_queue):
    cookies = {
    'SID': 'RAhQuUxco49lz_JuQKTMJF1vD5Ws_ntbdFi-aCEQulDmuo-f0AD3MS1KLdR5ii0EEbHsPQ.',
    '__Secure-1PSID': 'RAhQuUxco49lz_JuQKTMJF1vD5Ws_ntbdFi-aCEQulDmuo-fRId8w_ov0gNbe2WfYLXHJw.',
    '__Secure-3PSID': 'RAhQuUxco49lz_JuQKTMJF1vD5Ws_ntbdFi-aCEQulDmuo-fL8GtPGMYfwrkm1OKxDwBgw.',
    'HSID': 'A5yFJ1o_OQH4-oMcy',
    'SSID': 'A1sZWi67aroLKEAl_',
    'APISID': '9Gcx9mcatg2EKA0G/AAkGsXvONkOl28s6g',
    'SAPISID': 'bUKBKCxHWdqxjHy-/AEwiGq_OSUsKXlQH6',
    '__Secure-1PAPISID': 'bUKBKCxHWdqxjHy-/AEwiGq_OSUsKXlQH6',
    '__Secure-3PAPISID': 'bUKBKCxHWdqxjHy-/AEwiGq_OSUsKXlQH6',
    'SEARCH_SAMESITE': 'CgQIg5cB',
    'OTZ': '6798326_76_76_104100_72_446760',
    'AEC': 'AakniGPSfwXyDy73AQOEz2cdxE1lsRb1qTTnGRd4j1yazNphFZ_p2ODzXw',
    '1P_JAR': '2022-12-09-19',
    'NID': '511=TOcTSpKErcIF7YOqTwar_h5dE42ptLqHC1SMwZHHfEsPFlULf-gcWiwmIMc-Ckqfu7Ix1IGI3SJ6Wf2jzgKkxPzjrQ1iO6Hn_Wd1wDznPNSd_ZXqhbp28txp0Q65tsKI-b9jWWrPCuuVs8onkc3N0jgRdy7LHEgySPh3yDQCne8P_t4uoayEAKGtrJvjt9bqpt45xpyZyp6C0GHYXH-gCgp4wj_HOD7jbb6Ntth9KvNkCGrG3FcAZa42Et0Vh1g',
    'SIDCC': 'AIKkIs1au3XEXYNAGEQOirYQD8B3LP27wBFhltbi4QDN55UvS7llqUPzp72AEm6LSSUN49Eno9w',
    '__Secure-1PSIDCC': 'AIKkIs1o7zy9uJOy6VOjrlMSOdodSTEGSPGJpBVqBHnfeXOcPGSlYkbwxnvgWfunhZWsZ1AieN0',
    '__Secure-3PSIDCC': 'AIKkIs2jb_QEtTTu47__c4vEk90MWH1GyaDhxYu2u5AVTopmaiZNy8ip__XhujoRPn1xtXmvwC0',
    }

    headers = {
        'authority': 'ogs.google.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'SID=RAhQuUxco49lz_JuQKTMJF1vD5Ws_ntbdFi-aCEQulDmuo-f0AD3MS1KLdR5ii0EEbHsPQ.; __Secure-1PSID=RAhQuUxco49lz_JuQKTMJF1vD5Ws_ntbdFi-aCEQulDmuo-fRId8w_ov0gNbe2WfYLXHJw.; __Secure-3PSID=RAhQuUxco49lz_JuQKTMJF1vD5Ws_ntbdFi-aCEQulDmuo-fL8GtPGMYfwrkm1OKxDwBgw.; HSID=A5yFJ1o_OQH4-oMcy; SSID=A1sZWi67aroLKEAl_; APISID=9Gcx9mcatg2EKA0G/AAkGsXvONkOl28s6g; SAPISID=bUKBKCxHWdqxjHy-/AEwiGq_OSUsKXlQH6; __Secure-1PAPISID=bUKBKCxHWdqxjHy-/AEwiGq_OSUsKXlQH6; __Secure-3PAPISID=bUKBKCxHWdqxjHy-/AEwiGq_OSUsKXlQH6; SEARCH_SAMESITE=CgQIg5cB; OTZ=6798326_76_76_104100_72_446760; AEC=AakniGPSfwXyDy73AQOEz2cdxE1lsRb1qTTnGRd4j1yazNphFZ_p2ODzXw; 1P_JAR=2022-12-09-19; NID=511=TOcTSpKErcIF7YOqTwar_h5dE42ptLqHC1SMwZHHfEsPFlULf-gcWiwmIMc-Ckqfu7Ix1IGI3SJ6Wf2jzgKkxPzjrQ1iO6Hn_Wd1wDznPNSd_ZXqhbp28txp0Q65tsKI-b9jWWrPCuuVs8onkc3N0jgRdy7LHEgySPh3yDQCne8P_t4uoayEAKGtrJvjt9bqpt45xpyZyp6C0GHYXH-gCgp4wj_HOD7jbb6Ntth9KvNkCGrG3FcAZa42Et0Vh1g; SIDCC=AIKkIs1au3XEXYNAGEQOirYQD8B3LP27wBFhltbi4QDN55UvS7llqUPzp72AEm6LSSUN49Eno9w; __Secure-1PSIDCC=AIKkIs1o7zy9uJOy6VOjrlMSOdodSTEGSPGJpBVqBHnfeXOcPGSlYkbwxnvgWfunhZWsZ1AieN0; __Secure-3PSIDCC=AIKkIs2jb_QEtTTu47__c4vEk90MWH1GyaDhxYu2u5AVTopmaiZNy8ip__XhujoRPn1xtXmvwC0',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-client-data': 'CI62yQEIo7bJAQjBtskBCKmdygEIsI/LAQiTocsBCOiyzAEI1NjMAQjG4cwBCPLtzAEI9PHMAQiN98wBCMz5zAEI4vnMAQi0+swBCKT7zAEI7//MAQiGgc0BGNfszAE=',
    }

    while True:
        url = input_queue.get()
        if url is None:
            break

        print(f"URL :  {url}\n")
        try:
            response = requests.get(url, cookies=cookies, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            headers = response.headers
            print(f"title : {soup.title.string}\n")
        except Exception as e:
            print(f"Exception in getting header : {e}")


def main():
    number_of_workers = 8
    with open("top-100.csv", "r") as f:
        data = f.read()
    urls = data.split("\n")

    input_queue = Queue()
    workers = []

    # now create workers with for loop

    for i in range(number_of_workers):
        p = Process(target=worker, args=(input_queue, ))
        workers.append(p)
        p.start()
    
    # distribution of workers

    for url in urls:
        url = "https://"+url.split(",")[1]
        input_queue.put(url)

    # ask worker to quit

    for w in workers:
        input_queue.put(None)

    # wait for worker to quit
    for w in workers:
        w.join()
    print('Done')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("------ %s seconds ------" % (time.time() - start_time))
