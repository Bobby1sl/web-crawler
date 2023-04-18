html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 

                <li class="item-2">
                    <a href="link2.html">第二个</a>
                </li> 

                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 

                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li> 

                <li class="item-5">
                    <a href="link5.html">第五个</a> 
                </li>
            </ul>
        </div>
"""

import parsel

selector = parsel.Selector(html_str)

# 获取第四个<a>标签, 并获取其href属性值
result = selector.xpath('//li[1]').getall()
print(result)


"""
    xpath语法中
    对于同级标签, 如果要精确定位第几个, 可以用[]定位, 考好内填写数字, 类似于索引, 从1开始
"""