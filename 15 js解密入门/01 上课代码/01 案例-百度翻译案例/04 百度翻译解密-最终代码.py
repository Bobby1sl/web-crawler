import execjs
import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

headers = {
    'Acs-Token': '1683808254994_1683808421275_Wlty7hdj60d6KA/u9ruUCuViZUxTcZtXu6rMxacQng7jd+aAhtnFYklYsZP6S62zxSdEi1yqVWzY6Pc+TRKX5YsaTroE9fUI1eKL2kPChJK0yDvHoq7YS02KEQ4XTv91E//7FnDOSjlLv/Si98qqe2ihrGt5M/bK5NwVA6zDZIRuC83kF8PRik2ZyTL8TnK+qSQVY3mVpfo9GccYNNsDqOFhwbejTjGH2CyuPFSrkD9NgCnDwApbKd1VXv0ek7E+VvDsNsdPYfPaELeRQJQcoAaVSqN42pZXCyVLYnJvdoxWyxg4YTNYaUG/kiS7u4VRWqDrwobf3jKuQ+ofXh3ICLvru17EpAoyItrZzKvXJnYQLXLv2zBDaZRfX4E6wGdcQoSQrLrLlcshyuz6VW1GBDG02zAAkkZkCWzMcYLhu9+3ZgXr5OJTCsskXaIl+fC/7r+SV3eQJ31ONZDOt4/GWiX2nswG2n6+AMsl1m4/L4A=',
    'Cookie': 'BIDUPSID=A8D9EA340531252B16551CBD43A8D395; PSTM=1681976911; BAIDUID=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; newlogin=1; ZFY=7lff057ilIi2n87UZz:AEQLgMCi3N17GW0F7n8elnQtE:C; BAIDUID_BFESS=A8D9EA340531252BDEF2C13A73AFA5E7:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=200h01ak0g80al2584a180es1i5n42o1n; H_PS_PSSID=38516_36550_38529_38469_38468_38591_38486_26350_38545; PSINO=6; delPer=0; RT="z=1&dm=baidu.com&si=uie246tceog&ss=lhj3ygvm&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=10m&hd=10v"; BCLID=8671131649299938091; BCLID_BFESS=8671131649299938091; BDSFRCVID=vgPOJexroG07VWbfVQHvIGta5LweG7bTDYrEOwXPsp3LGJLVFe3JEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=vgPOJexroG07VWbfVQHvIGta5LweG7bTDYrEOwXPsp3LGJLVFe3JEG0Pts1-dEu-S2OOogKKLmOTHpKF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvDqTrP-trf5DCShUFsqpQmB2Q-XPoO3KtbSx3PbljGy-0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0tLeWeTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD89DjKKD6PVKgTa54cbb4o2WbCQbJ3m8pcN2b5oQTOW3RJaKq5IWTcAK-bqJlRbeq06-lOUWJDkXpJvQnJjt2JxaqRC3JK5Ol5jDh3MKToDb-oteltHB2Oy0hvcBn6cShnxyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f6DOJnkj3O; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvDqTrP-trf5DCShUFsqpQmB2Q-XPoO3KtbSx3PbljGy-0PQpOKtx7f5mkf3fbgy4op8P3y0bb2DUA1y4vp0tLeWeTxoUJ2-KDVeh5Gqq-KXU4ebPRiWPr9QgbjahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD89DjKKD6PVKgTa54cbb4o2WbCQbJ3m8pcN2b5oQTOW3RJaKq5IWTcAK-bqJlRbeq06-lOUWJDkXpJvQnJjt2JxaqRC3JK5Ol5jDh3MKToDb-oteltHB2Oy0hvcBn6cShnxyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f6DOJnkj3O; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1683808253; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1683808253; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_NjFhM2I0NmI5YjY2ZDUxOTMxOGVkYTQ1MGQ2MTk2YTI4MTRiNGFhZDBkMTE0MmFhODllMmM2ZmNlZmY3Yjg5YmQ5YWRkY2JmMDE0ZTJlNzNlYTcyZDc1MzIxM2ZjMGNlZmVkY2UyM2E5NWE3MmNmNGZlZDczZWI3NDBkNTgyOTMzOGIxNjg3MzI2ZGJlMThjMDE2MTM3NDUxMGIzOWQ1NA==',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

while True:
    word = input('请输入要翻译的汉字<输入0退出>:')
    if word == '0':
        break

    """读取js代码"""
    with open('02 百度翻译js解密.js', mode='r', encoding='utf-8') as f:
        js_code = f.read()

    """编译js代码"""
    compile_result = execjs.compile(js_code)
    # print(compile_result)

    """调用编译好js代码中的函数"""
    result = compile_result.call('fanyi', word)

    data = {
        'from': 'zh',
        'to': 'en',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': result,
        'token': '351b986af9e8a703056ff2f022cdf830',
        'domain': 'common',
    }

    response = requests.post(url=url, data=data, headers=headers)
    json_data = response.json()
    print(json_data['trans_result']['data'][0]['dst'])



"""
js代码逆向思路:

    找加密的数据: 1.查询参数 2.请求参数 3.请求头字段信息 4.数据包返回的数据加密了
    
    通过数据包逆向分析, 找到js加密的主要函数逻辑, 执行函数
    
    根据报错, 缺哪补哪
    
    
做js解密必须得学习js原生语法
"""