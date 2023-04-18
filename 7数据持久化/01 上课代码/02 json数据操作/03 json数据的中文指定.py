import json

data = {
    'name': 'ACCE',
    'shcool': '青灯',
    'price': 5120,
}

# ensure_ascii=False  不使用默认的unicode编码
json_str = json.dumps(data, ensure_ascii=False)

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json_str)