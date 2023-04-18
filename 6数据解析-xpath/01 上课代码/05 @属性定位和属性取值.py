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
result = selector.xpath('//a[@href="link4.html"]').getall()
print(result)

result = selector.xpath('//a[@href="link4.html"]/@href').getall()
print(result)


"""
    xpath语法中
    @ 有两个用途
        1. 根据标签特有的属性<class  href  src id title ...>精确定位
        2. 可以根据已经定位好的标签, 指定标签内属性的名字, 提取其属性值
"""