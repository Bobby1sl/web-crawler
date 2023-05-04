import base64
import requests
from constants import KUAI_USERNAME, KUAI_PASSWORD


def base64_api(img, typeid):
    """
    识别验证码主函数
    :param img: 图片路径
    :param typeid: 识别类型
    :return:
    """
    # 打开图片, 把图片转化成字符串形式
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()

    data = {"username": KUAI_USERNAME, "password": KUAI_PASSWORD, "typeid": typeid, "image": b64}
    result = requests.post("http://api.kuaishibie.cn/predict", data=data).json()
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


if __name__ == "__main__":
    img_path = "yzm.png"
    result = base64_api(img=img_path, typeid=7)
    print(result)
