import json  # 内置模块


data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)

with open('data.json', mode='r', encoding='utf-8') as f:
    print(f.read())
