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

# 跨节点, 获取所有的<a>标签
result = selector.xpath('//a').getall()
print(result)

"""
    xpath语法中
    //  表示跨节点提取, 不用考虑标签的结构, 用的多
    跨节点可以用于xpath语法中任意的语法位置
"""