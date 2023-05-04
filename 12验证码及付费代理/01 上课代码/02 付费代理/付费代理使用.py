import requests

def get_proxy():
    url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=2&sb=&mr=2&sep=0'
    response = requests.get(url=url)
    json_data = response.json()
    print(json_data)

    ip = json_data['data'][0]['ip']
    port = str(json_data['data'][0]['port'])

    proxies = {
      "http": "http://" + ip + ':' + port,
      "https": "http://"  + ip + ':' + port,
    }
    print('构建好的代理:', proxies)
    return proxies


if __name__ == '__main__':
    proxies = get_proxy()

    response = requests.get(url='https://www.baidu.com', proxies=proxies)
    print(response.text)

