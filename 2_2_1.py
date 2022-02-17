#!/usr/bin/env python
'''
Реализуйте алгоритм для нахождения в односвязном списке k-го элемента
с конца.
'''
from typing import Optional, List

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"[{self.data}]-> {self.next}"
    
def findElementRecursWithHelper(head: Optional[Node], k: int) -> Optional[Node]:
    fast = head
    slow = head
    return helper(fast, slow, k)

def helper(f, s, k) -> Optional[Node]:
    if f == None:
        return s
    if k == 0:
        return helper(f.next, s.next, k)
    else:
        return helper(f.next, s, k - 1)
    return s

######################################################################
if __name__ == '__main__':
    ll = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    #print(ll)
    print(findElementRecursWithHelper(ll, 3))
