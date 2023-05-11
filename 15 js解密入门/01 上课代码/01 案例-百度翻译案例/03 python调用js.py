import execjs  # pip install pyexecjs 安装的模块名--->pyexecjs; 导入的模块名是-->>execjs


"""读取js代码"""
with open('02 百度翻译js解密.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

"""编译js代码"""
compile_result = execjs.compile(js_code)
print(compile_result)

"""调用编译好js代码中的函数"""
result = compile_result.call('fanyi', '你好')
print(result)