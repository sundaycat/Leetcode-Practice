## 206

### recurison

**怎么构建回归**
1. 结束条件是什么(base case)
2. 需要向上一层返回什么, 本层要做什么, 要向下一层传递什么

``` python
from __future__ import print_function

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print() 

def reverse_list(head):
    return helper_2(None, head)

# reverse the linklist from left to right, tail resusion
def helper(pre, cur):
    if cur is None:
        return pre
    
    temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp
    
    return helper(pre, cur)

# reverse the linklist from left to right, tail recursion(simplifer)
def helper_1(pre, cur):
    if cur is None:
        return pre
    
    next = cur.next
    cur.next = pre
    return helper(cur, next)

# reverse the linklist from right to left, non-tail recursion
def helper_2(pre, cur):
    if cur is None:
        return pre

    new_head = helper_2(cur, cur.next)
    cur.next = pre
    return new_head



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.print_list()
rs = reverse_list(head)
rs.print_list()
```


## 876, 143, 23
### fast slow pointer

1. 改变返回值, 模板的变化.
