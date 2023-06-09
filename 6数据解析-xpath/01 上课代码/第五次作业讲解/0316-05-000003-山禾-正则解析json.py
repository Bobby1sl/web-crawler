"""
1. 采集网址 https://haokan.baidu.com/tab/gaoxiao_new

2. 采集目标
	- 采集当前页面里面的数据
	- 需要需要采集以下数据:
		title 视频标题
		duration 视频时长
		fmplaycnt 播放量

    - 用正则表达式采集
"""
import re

import requests


url = 'https://haokan.baidu.com/web/video/feed?tab=gaoxiao_new&act=pcFeed&pd=pc&num=22&shuaxin_id=16815598400000'
# authority 相当于 host
headers = {
    'authority': 'haokan.baidu.com',
    'cookie': 'PSTM=1657895499; BIDUPSID=D26C29435949C22624426B7C5A1F52F3; BAIDUID=963EC08DDD8CA5647A50D2ED99D0CCF2:SL=0:NR=10:FG=1; H_WISE_SIDS=219946_232280_231979_222624_234085_234044_219623_232777_234572_238145_234020_230584_232357_131861_238265_239761_234208_114551_232244_219566_234296_234426_235174_235513_236239_238755_240305_237837_236538_236653_239947_240889_240939_240447_240466_240742_241208_241177_240782_241248_240597_241282_240649_241296_241328_241349_240035_238226_241460_216839_224267_227932_213356_229967_211986_239898_238444_215730_237893_214799_239101_238511_223064_219943_238507_213033_228650_229154_234781_204916_226628_241245_241565_238073_240905_230288_239492_232628_241757_241794_241153_234433_241815_241850_241864_240204_241970_240734_241780_232630_242055_242218_242224_242271_242379_242374_241601_242267_241892_241698_242473_241785_222222_237964_237821_241548_242489; H_WISE_SIDS_BFESS=219946_232280_231979_222624_234085_234044_219623_232777_234572_238145_234020_230584_232357_131861_238265_239761_234208_114551_232244_219566_234296_234426_235174_235513_236239_238755_240305_237837_236538_236653_239947_240889_240939_240447_240466_240742_241208_241177_240782_241248_240597_241282_240649_241296_241328_241349_240035_238226_241460_216839_224267_227932_213356_229967_211986_239898_238444_215730_237893_214799_239101_238511_223064_219943_238507_213033_228650_229154_234781_204916_226628_241245_241565_238073_240905_230288_239492_232628_241757_241794_241153_234433_241815_241850_241864_240204_241970_240734_241780_232630_242055_242218_242224_242271_242379_242374_241601_242267_241892_241698_242473_241785_222222_237964_237821_241548_242489; BDUSS=NSZGdjV0h-RkV3LVFyRGNGaUxaaWZ6fnF2T041VGhxOHNSQ2NhNWpaWGFHaVJrSUFBQUFBJCQAAAAAAQAAAAEAAADlydJEx-C1xr3M0~1WSVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANqN~GPajfxjen; BDUSS_BFESS=NSZGdjV0h-RkV3LVFyRGNGaUxaaWZ6fnF2T041VGhxOHNSQ2NhNWpaWGFHaVJrSUFBQUFBJCQAAAAAAQAAAAEAAADlydJEx-C1xr3M0~1WSVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANqN~GPajfxjen; BAIDUID_BFESS=963EC08DDD8CA5647A50D2ED99D0CCF2:SL=0:NR=10:FG=1; BA_HECTOR=8k8h0lag2k818484008404f01i3l17d1n; ZFY=DQGVNm9J85cHlTa9bGNHiaqrU:BUlyl:BoIp4VvVA6BXI:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=6; delPer=0; H_PS_PSSID=38516_36558_38470_38349_38468_37920_37709_26350_38185; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; __bid_n=185103f34913964fcf4207; FPTOKEN=0yTitxIj5OTGQnH0nxxy1wEqeq/+XwFyLwOKq/dHIw3XjrgEVP81R/18xzZRnbNkK3EzvyPHeZeJqDmbNS2YX4FKF6aK4zEPuMAme3fMvDqrV+2G8fBUwDANW80CozqbvGoH3ZFDE9tZbe6tjJqXzYdWU0tWGcl8FFQ9rmuUF7suLY+IEbDPsUyUsFjsPZafZyIPU4ivnMsOnYz9j/Lq/wsjPBTcsoLyx1LWUQizgAsW9iqipIv016kqrmPerwTqKKDp//7GNBOU897Pu6alJPBrbR7PfytY1RR+F2oY7HyG02rdbpM7kBc7s0TySguznWr157fgEWTZ16pFSzFMGGQv1fWfkgJaiqQCuPemdmF1ztQ3bP4CYIFYtwcCDO045Xuo7j5/916OogXtMgC3mw==|1N+aqfY8u9/lA7fRrBVsIU2E+pnfd6jVS9JNdk728ew=|10|60fca9bcb34551cc584acff2c9f449d9; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1681559694; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1681559740; ab_sr=1.0.1_MThiNGRmNzA0MDk2M2FjMDUxMTBhZGVhYjRmNjY0ZTE0Y2ZjNjhhYzI3MTcwMzE3MDY1NDg2ZmRiN2EwMmIzMGU2OTcxNjgzODc4YjY3NzdjZTkwNDc2NGQ4ZDBlODVkMTc4MzdjMjJjMzVjZGM5NTJjOWY5ODNkNGQzNzYzZWQ0MTdkMjFjNjQxZGJjNmI5NTJlYTkyYzMyY2E5NjcwMQ==; reptileData=%7B%22data%22%3A%22ff61c3014bf0e1a845df1008a5679b821358277f678467f6de74b65d1c02a058faa808a53c8a7a07f3246f73938048aea61e81a29957df52a865e33e4bb695fc78b275920e65cdcdd04f9974b7e992c5dabd649831f5768f93ba1eb65ac8227f%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22e8526e95%22%7D; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=14be1556-369e-4043-9fe8-ec4e67d3a921&ss=lghx838a&sl=2&tt=308&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=11jw&ul=35v2&hd=36d4"',
    'referer': 'https://haokan.baidu.com/tab/gaoxiao_new',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}
response = requests.get(url=url, headers=headers)
json_data = response.json()
print(json_data)

# {'id': '7522600232560641187', 'title': '想不通寄沙算了', 'poster_small': 'https://f7.baidu.com/it/u=835550534,295367151&fm=222&app=106&f=JPEG@s_0,w_660,h_370,q_80', 'poster_big': 'https://f7.baidu.com/it/u=835550534,295367151&fm=222&app=106&f=JPEG@s_0,w_660,h_370,q_80', 'poster_pc': 'https://f7.baidu.com/it/u=835550534,295367151&fm=222&app=106&f=JPEG@s_0,w_660,h_370,q_80,f_auto', 'source_name': '黄小弟弟', 'play_url': 'http://vd3.bdstatic.com/mda-pbs5mxz8ye2mvam6/cae_h264/1677471715918961331/mda-pbs5mxz8ye2mvam6.mp4?v_from_s=hkapp-haokan-nanjing', 'duration': '00:58', 'url': 'https://haokan.hao123.com/v?vid=7522600232560641187&pd=pc&context=', 'show_tag': 0, 'publish_time': '02月27日', 'is_pay_column': 0, 'like': '0', 'comment': '5', 'playcnt': '63', 'fmplaycnt': '63次播放', 'fmplaycnt_2': '63', 'outstand_tag': '', 'previewUrlHttp': 'https://vd3.bdstatic.com/mda-pbs5mxz8ye2mvam6/cae_h264/1677471715918961331/mda-pbs5mxz8ye2mvam6.mp4?v_from_s=hkapp-haokan-nanjing&auth_key=1681561812-0-0-4c3e9b45e056d13181d097b32c43f420&bcevod_channel=searchbox_feed&pd=1&vt=1&cd=0&watermark=0&did=&logid=0011870368&vid=7522600232560641187&pt=0&appver=&model=&cr=0&abtest=peav_l52&sle=1&sl=500&split=437640', 'third_id': '1757590221133161', 'vip': 0, 'author_avatar': 'https://gips0.baidu.com/it/u=4139906786,2503853210&fm=3012&app=3012&autime=1681017077&size=b200,200&fmt=auto'}
# {'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)',.*? 'fmplaycnt': '(.*?)',.*?}
# \{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)',.*? 'fmplaycnt': '(.*?)',.*?\}
result = re.findall(
    "\{'id': '.*?', 'title': '(.*?)',.*?'duration': '(.*?)',.*? 'fmplaycnt': '(.*?)',.*?\}",
    str(json_data),
    re.S
)

print(result)

# 不规则的json数据, 只能用正则
