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

# 了解  contains 是模糊查询关键字
result = selector.xpath('//li[contains(@class,"item")]').getall()
print(result)


"""
    xpath语法中
        contains(@class,"item") 表示模糊查询
        @class  模糊查询class属性
        item    模糊查询class属性的关键字
"""