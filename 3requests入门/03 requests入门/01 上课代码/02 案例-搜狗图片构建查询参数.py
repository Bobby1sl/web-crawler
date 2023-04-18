import requests


url = 'https://pic.sogou.com/napi/pc/searchList'

for page in range(0, 97, 48):
    params = {
        'mood': '7',
        'dm': '0',
        'mode': '1',
        'start': str(page),
        'xml_len': '48',
        'query': '风景'
    }
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # print(json_data)

    data_list = json_data['data']['items']
    for data in data_list:
        img_url = data['picUrl']
        print(img_url)

    print('------------------------------------------------------------------\n')