import requests

headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'bid=JOjnHzNKNdU; __gads=ID=390a3a70609550e8-22df6781f5d10053:T=1649854444:RT=1649854444:S=ALNI_MZfvUIHFs1pOYgYSuPbsvh7fVT9Yw; ll="118267"; _vwo_uuid_v2=D9BE563CAF8DB68077925251DB19E9857|7ec7c5b6350ccfad2f138472e47a6641; _ga=GA1.2.1895635950.1649854444; gr_user_id=9841cb26-ad30-4da9-9fad-006c711b218f; __yadk_uid=u5mrwOVUZy3PATAVm4vE63U7vqrPrxRl; viewed="3283973"; __utmz=223695111.1680613115.33.24.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utma=30149280.1895635950.1649854444.1680615363.1680784782.41; __utmc=30149280; __utmz=30149280.1680784782.41.31.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1680784782; __gpi=UID=0000059a569b8b1b:T=1653051309:RT=1680784782:S=ALNI_MboLjGTnG9YzoGaau8maDJk8dhE7A; __utma=223695111.913704788.1649854444.1680613115.1680784802.34; __utmb=223695111.0.10.1680784802; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1680784802%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dx-C-aVNeY91eQhP_GTMra9eR8KjcM-NEEGtWy0rm8RCsFqHXq6HI1jASgtK_GOM0iQJfI0chWSJOSFjiBUiCv_%26wd%3D%26eqid%3Dbbf20d3700015d9e00000006642c1ef5%22%5D; _pk_id.100001.4cf6=5a00c88162b3f1ff.1649854444.34.1680784802.1680613115.; _pk_ses.100001.4cf6=*',
    # 'Host': 'movie.douban.com',
    # 'Pragma': 'no-cache',
    # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'document',
    # 'Sec-Fetch-Mode': 'navigate',
    # 'Sec-Fetch-Site': 'none',
    # 'Sec-Fetch-User': '?1',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

# headers 在构建请求的时候添加请求头
response = requests.get('https://movie.douban.com/top250', headers=headers)
html_data = response.text
print(html_data)

"""
为什么我请求不到数据?

    爬虫: 模拟客户端<手机app, 浏览器, 应用...>批量请求服务器<某度, 某歌, 某迅>数据
    
    服务器问题
        服务器挂了
        识别我的请求不正常
        请求被拦截
    
    个人问题
        没有请求的权限
        参数没构建好
        网络不好
        技术还不到位
"""

"""
常用的请求头字段
Origin: 资源的起始位置
User-Agent: 浏览器的身份标识
Host: 请求服务器的域名
Referer: 告诉服务器,我是从那个页面过来的<防盗链>
Cookies: 用户身份标识, 能不加就不加
"""
